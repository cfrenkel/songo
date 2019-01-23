import ctypes
import os
import time
from tkinter import ttk

import faces
from PIL import ImageTk, Image
import cv2
import tkinter as tk
import music_control
import speed_detection
import last_screen
from conclusion import Conclusion
import last_screen_tinkinter


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.newMaster = master
        self.master = master
        self.pack()

        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        back = tk.Frame(width=self.screensize[0], height=self.screensize[1], bg='white')

        self.lmain1 = tk.Label(self, text="hi")
        self.lmain1.grid(row=0, column=0)

        self.contm = 9

        self.calculate_face()

        myimage1 = tk.PhotoImage(file='songo.png')
        a = tk.Label(self, image=myimage1)
        a.image = myimage1
        a.grid(row=1, column=0)

        # here

        back.pack()

        music_control.play_music('kapaim.mp3')
        # todo setvolume 0.1]\4/
        music_control.set_volume_start(0)

        self.flag = False
        self.counter = 500
        self.cap = cv2.VideoCapture(0)

        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")

        self.bytes = 0
        self.maxbytes = 0
        self.mph = 0

        self.progress["value"] = 5000
        self.maxbytes = 50000
        self.progress["maximum"] = 50000

        self.progress.grid(row=1, column=1)


        self.video_stream()

    def read_bytes(self, mph):
        '''simulate reading mph bytes; update progress bar'''
        self.bytes += mph
        self.progress["value"] = self.bytes
        if self.bytes >= self.maxbytes:
            self.bytes = 0


    def calculate_face(self):

        File = os.listdir('extracted/')

        size = len(File)
        mini = min(size, 9)
        img = []
        for i in range(mini):
            FileDir = 'extracted/' + File[i]
            img.append(FileDir)
            print(FileDir)

        i = 0
        self.in_grid = tk.Frame(self, bg='white')

        for im in img:
            i += 1
            self.calc(i, im,self.in_grid)
            # self.myimage = tk.PhotoImage(file=im)
            # self.bb = tk.Label(self, image=self.myimage, bg='red')
            # self.bb.image = self.myimage
            # r, c = self.calc(i)
            #
            # if r == -1 and c == -1:
            #     break
            # self.bb.grid(row=r, column=c)
        self.in_grid.grid(row=0,column=1)

    def calc(self, i, im, in_grid):

        if i == 0:
            self.myimage0 = tk.PhotoImage(file=im)
            self.bb0 = tk.Label(in_grid, image=self.myimage0, bg='red')
            self.bb0.image = self.myimage0
            self.bb0.grid(row=0, column=0)
        if i == 1:
            self.myimage1 = tk.PhotoImage(file=im)
            self.bb1 = tk.Label(in_grid, image=self.myimage1, bg='red')
            self.bb1.image = self.myimage1
            self.bb1.grid(row=0, column=1)
        if i == 2:
            self.myimage2 = tk.PhotoImage(file=im)
            self.bb2 = tk.Label(in_grid, image=self.myimage2, bg='red')
            self.bb2.image = self.myimage2
            self.bb2.grid(row=1, column=0)
        if i == 3:
            self.myimage3 = tk.PhotoImage(file=im)
            self.bb3 = tk.Label(in_grid, image=self.myimage3, bg='red')
            self.bb3.image = self.myimage3
            self.bb3.grid(row=1, column=1)


    def video_stream(self):
        _, frame1 = self.cap.read()
        self.contm, mph = speed_detection.speed_detection(frame1, self.contm)
        if (mph > self.mph):
            self.read_bytes(mph)
        else:
            self.read_bytes(mph - self.mph)
        self.mph = mph
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)

        self.flag = self.music_on()
        if self.flag:
            self.lmain1.after(1, self.video_stream)
        else:
            print("finish")
            music_control.play_music('succ.mp3')
            time.sleep(5)
            self.action_collage()
            music_control.play_music('succ.mp3')
            # self.cap1.release()
            self.cap1 = cv2.VideoCapture('videoplayback.mp4')
            music_control.play_music('succ.mp3')
            self.video_stream1()

    def action_collage(self):


        File = os.listdir('images_collection/')
        lf = []
        for i in range(9):
            lf.append('images_collection/' + File[i])
        imgee = last_screen.last_screen(lf)

        # ----------------------------------
        imgee = last_screen.small_image1(imgee)
        imgee.save('collage9.png')

        self.destroy_faces()

        self.myimage2 = tk.PhotoImage(file='collage9.png')
        print("here ..........")
        self.b = tk.Label(self, image=self.myimage2, bg = 'red')
        self.b.image = self.myimage2
        self.b.grid(row=0, column=1)


    def destroy_faces(self):
        self.in_grid.destroy()
        self.progress.destroy()

    def dest(self,i):
        if i == 0:
            self.bb0.config(image='')
        if i == 1:
            self.bb1.config(image='')

        if i == 2:
            self.bb2.config(image='')

        if i == 3:
            self.bb3.config(image='')

        #self.b.grid(row=0, column=2)
        #
        # self.b = tk.Label(self, bg='red').config(image=None)
        # self.b.grid(row=0, column=3)
        #
        # self.b = tk.Label(self, bg='red').config(image=None)
        # self.b.grid(row=0, column=4)

        # ------------------------------------

    def video_stream1(self):
        print("here")
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.flag = self.continue_movie()
        if not self.flag:
            self.lmain1.after(1, self.video_stream1)
        else:
            print("finish")
            music_control.play_music('succ.mp3')
            time.sleep(5)
            self.cap1.release()
            cv2.destroyAllWindows()
            music_control.play_music('succ.mp3')
            time.sleep(5)

            # last = ImageWindow()
            # self.conclusion = Conclusion(self.newMaster, speed=[23, 54, 6, 88, 34, 32, 5, 7], volume=[4, 33, 8,2,67,98,46,3])

    def continue_movie(self):
        print(self.counter)
        if self.counter == 0:
            return True
        self.counter -= 1

    def music_on(self):
        return music_control.get_busy()


def is_one_not_dance(mp_list):
    pass


def conclusion(list_of_mph):
    pass


def calaulate_volum(avg):
    print("========vol=================")

    if avg > 500:
        music_control.set_volume(1)
        print('1')
    elif avg <= 500 and avg > 400:
        print('0.1')
        music_control.set_volume(0.9)
    elif avg <= 400 and avg > 320:
        music_control.set_volume(0.8)
        print('0.8')
    elif avg <= 320 and avg > 250:
        music_control.set_volume(0.7)
        print('0.7')
    elif avg <= 250 and avg > 210:
        music_control.set_volume(0.7)
        print('0.6')
    elif avg <= 210 and avg > 170:
        music_control.set_volume(0.7)
        print('0.5')
    elif avg <= 170 and avg > 120:
        music_control.set_volume(0.4)
        print('0.4')
    elif avg <= 120 and avg > 70:
        music_control.set_volume(0.3)
        print('0.3')
    elif avg <= 70 and avg > 30:
        music_control.set_volume(0.2)
        print('0.2')
    elif avg <= 30 and avg > 1:
        music_control.set_volume(0.1)
        print('0.1')
    elif avg <= 1:
        music_control.set_volume(0)
        print('0')
