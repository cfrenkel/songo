import cv2
import numpy as np
import time
import copy
from datetime import datetime
import music_control

from kalman_filter import KalmanFilter
from tracker import Tracker


def calaulate_volum(avg):
    print("========vol=================")

    if avg > 500:
        music_control.set_volume(1)
        print('1')
    elif avg <= 500 and avg > 400:
        print('0.9')
        music_control.set_volume(0.9)
    elif avg <= 400 and avg > 320:
        music_control.set_volume(0.8)
        print('0.8')
    elif avg <= 320 and avg > 250:
        music_control.set_volume(0.7)
        print('0.7')
    elif avg <= 250 and avg > 210:
        music_control.set_volume(0.6)
        print('0.6')
    elif avg <= 210 and avg > 120:
        music_control.set_volume(0.5)
        print('0.5')
    elif avg <= 120 and avg > 80:
        music_control.set_volume(0.4)
        print('0.4')
    elif avg <= 80 and avg > 70:
        music_control.set_volume(0.3)
        print('0.3')
    elif avg <= 70 and avg > 30:
        music_control.set_volume(0.2)
        print('0.2')
    elif avg <= 30 and avg > 18:
        music_control.set_volume(0.1)
        print('0.1')
    elif avg <= 18:
        music_control.set_volume(0)
        print('0')

FPS = 30
'''
    Distance to line in road: ~0.025 miles
'''
# ToDo small the param
ROAD_DIST_MILES = 0.025

'''
    Speed limit of urban freeways in California (50-65 MPH)
'''
# ToDo small the param
HIGHWAY_SPEED_LIMIT = 40

# Initial background subtractor and text font
fgbg = cv2.createBackgroundSubtractorMOG2()
font = cv2.FONT_HERSHEY_PLAIN

centers = []

# y-cooridinate for speed detection line
Y_THRESH = 242

blob_min_width_far = 6
blob_min_height_far = 6

blob_min_width_near = 18
blob_min_height_near = 18

frame_start_time = None

# Create object tracker
tracker = Tracker(80, 3, 2, 1)

# Capture livestream

# # todo playMusic
# music_control.play_music('mysong.mp3')
# # todo setvolume 0.1
# music_control.set_volume(0.1)

def speed_detection(frame, counter_image):
    if not music_control.get_busy():
        # print(All_mph_list)
        # conclusion(All_mph_list)
        return counter_image, 0

    centers = []
    frame_start_time = datetime.utcnow()

    orig_frame = copy.copy(frame)

    #  Draw line used for speed detection
    cv2.line(frame, (0, Y_THRESH), (640, Y_THRESH), (255, 0, 0), 2)

    # Convert frame to grayscale and perform background subtraction
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(gray)

    # Perform some Morphological operations to remove noise
    kernel = np.ones((4, 4), np.uint8)
    kernel_dilate = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    dilation = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel_dilate)

    # todo
    _, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    avg = 0
    if len(contours) < 10:
        calaulate_volum(5)
    else:
        # Find centers of all detected objects
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            if y > Y_THRESH:
                if w >= blob_min_width_near and h >= blob_min_height_near:
                    center = np.array([[x + w / 2], [y + h / 2]])
                    centers.append(np.round(center))

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                if w >= blob_min_width_far and h >= blob_min_height_far:
                    center = np.array([[x + w / 2], [y + h / 2]])
                    centers.append(np.round(center))

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if centers:
            tracker.update(centers)

            mph = 0
            counter = 0
            mph_list = []
            for vehicle in tracker.tracks:
                if len(vehicle.trace) > 1:
                    for j in range(len(vehicle.trace) - 1):
                        # Draw trace line
                        x1 = vehicle.trace[j][0][0]
                        y1 = vehicle.trace[j][1][0]
                        x2 = vehicle.trace[j + 1][0][0]
                        y2 = vehicle.trace[j + 1][1][0]

                        cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)

                    try:
                        '''
                            TODO: account for load lag
                        '''

                        trace_i = len(vehicle.trace) - 1

                        trace_x = vehicle.trace[trace_i][0][0]
                        trace_y = vehicle.trace[trace_i][1][0]

                        # Check if tracked object has reached the speed detection line
                        if True:
                            # cv2.putText(frame, 'I PASSED!', (int(trace_x), int(trace_y)), font, 1, (0, 255, 255), 1,
                            #             cv2.LINE_AA)
                            vehicle.passed = True

                            load_lag = (datetime.utcnow() - frame_start_time).total_seconds()

                            time_dur = (datetime.utcnow() - vehicle.start_time).total_seconds() - load_lag
                            time_dur /= 60
                            time_dur /= 60

                            if counter_image > 0 and music_control.get_volume() > 0.6:
                                print(counter_image)
                                # print(counter_image)
                                counter_image -= 1
                                cv2.imwrite(f'images_collection/speeding_%s.png' % counter_image, orig_frame)

                            vehicle.mph = ROAD_DIST_MILES / time_dur
                            mph_list.append(vehicle.mph)

                            # If calculated speed exceeds speed limit, save an image of speeding car
                            if vehicle.mph > HIGHWAY_SPEED_LIMIT:
                                mph += int(vehicle.mph)
                                counter += 1

                        if vehicle.passed:
                            mph += int(vehicle.mph)
                            counter += 1

                    except:
                        pass

            # todo setvolume
            if counter != 0:
                avg += mph / counter
                calaulate_volum(avg)
    return counter_image, avg

