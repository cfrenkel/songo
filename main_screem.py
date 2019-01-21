import tkinter as tk
from PIL import ImageTk, Image
import cv2
import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.lmain1 = tk.Label(self, text="hi")
        self.lmain1.grid(row = 0, column = 0)

        self.flag = False

        self.cap1 = cv2.VideoCapture(0)
        self.video_stream()

    def video_stream(self):
        print("here")
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.flag = self.music_on()
        if not self.flag:
            self.lmain1.after(1, self.video_stream)
        else:



    def music_on(self):
        return False
