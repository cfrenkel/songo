import Algorithmia
from PIL import ImageTk, Image
import cv2
import tkinter as tk
import imageio

root = tk.Tk()


class OpenScreen(tk.Frame):
    def __init__(self):
        self.lmain1 = tk.Label(root, text="hi")
        self.lmain1.pack()

        # self.canvas = tk.Canvas(width=300, height=200, bg='yellow')
        # self.canvas.grid(row=0, column=1)

        self.cap1 = cv2.VideoCapture(0)
        self.video_stream()
        self.flag = False
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

    def analyze_picture(self, image):
        print("here2")
        input = "first.png"
        client = Algorithmia.client('simpNpbFDF0YSVFxvB9WIWWTTLV1')
        algo = client.algo('deeplearning/GenderClassification/2.0.0')
        print(algo.pipe(input).result)
        return True


o = OpenScreen()
