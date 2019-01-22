import ctypes
import time

from PIL import ImageTk, Image
from main_screem import MainWindow
import cv2
import tkinter as tk
import detect_face
import music_control

root = tk.Tk()


class OpenScreen(tk.Frame):
    def __init__(self):
        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        back = tk.Frame(width=self.screensize[0], height=self.screensize[1], bg='white')

        myimage = tk.PhotoImage(file='logo1.png')
        label = tk.Label(image=myimage)
        label.image = myimage  # the reference
        label.pack(side=tk.LEFT)

        self.lmain1 = tk.Label(root, text="hi")
        self.lmain1.pack(side=tk.LEFT)

        myimage1 = tk.PhotoImage(file='newewl.png')
        label1 = tk.Label(image=myimage1)
        label1.image = myimage  # the reference
        label1.pack(side=tk.LEFT)

        back.pack()

        self.flag = False

        self.count = 150
        self.count1 = 0

        self.cap1 = cv2.VideoCapture(0)

        self.video_stream()

        root.mainloop()

    def video_stream(self):
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.flag = self.analyze_picture(frame1)
        if not self.flag:
            self.lmain1.after(1, self.video_stream)
        else:
            music_control.play_music('open.mp3')
            time.sleep(6)
            self.cap1.release()
            # todo pre
            root.destroy()
            main = MainWindow()

    def desplay_wellcome(self):
        pass

    def facing(self):
        detect_face.detect_faces('faces.png')

    def analyze_picture(self, frame):
        print("in analyze .... ")
        if self.count > 0:
            self.count -= 1
            return False
        if self.count == 0:
            cv2.imwrite('faces.png', frame)
            self.facing()
            return True



