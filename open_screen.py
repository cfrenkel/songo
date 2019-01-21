from PIL import ImageTk, Image
from main_screem import MainWindow
import cv2
import tkinter as tk

root = tk.Tk()


class OpenScreen(tk.Frame):
    def __init__(self):
        self.lmain1 = tk.Label(root, text="hi")
        self.lmain1.grid(row=0, column=0)

        myimage = tk.PhotoImage(file='dance.gif')
        label = tk.Label(image=myimage)
        label.image = myimage  # the reference
        label.grid(row=0, column=1)

        self.flag = False

        self.count = 100

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
        self.flag = self.analyze_picture()
        if not self.flag:
            self.lmain1.after(1, self.video_stream)
        else:
            self.cap1.release()
            root.destroy()
            main = MainWindow()

    def desplay_wellcome(self):
        pass

    def analyze_picture(self):
        if self.count == 0:
            return True
        self.count -= 1


