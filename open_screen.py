from PIL import ImageTk, Image
from main_screem import MainWindow
import cv2
import tkinter as tk

root = tk.Tk()


class OpenScreen(tk.Frame):
    def __init__(self):
        self.lmain1 = tk.Label(root, text="hi")
        self.lmain1.pack()

        # self.canvas = tk.Canvas(width=300, height=200, bg='yellow')
        # self.canvas.grid(row=0, column=1)

        self.flag = False

        self.count = 500
        self.cap1 = cv2.VideoCapture(0)
        self.video_stream()
        root.mainloop()

    def video_stream(self):
        print("here")
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.flag = self.analyze_picture(img1)
        if not self.flag:
            self.lmain1.after(1, self.video_stream)
        else:
            # todo --- wellcome message ---
            self.desplay_wellcome()
            root.destroy()
            main_window = MainWindow()

    def desplay_wellcome(self):
        pass

    def analyze_picture(self, image):
        if self.count == 0:
            return True
        self.count -= 1


