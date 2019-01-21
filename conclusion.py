import ctypes
import cv2
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Conclusion(tk.Frame):

    def __init__(self, master, speed, volume):
        super().__init__(master)
        self.master = master
        self.pack()

        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.speed, self.volume = speed, volume
        self.conclusion_wind()

    def video_stream(self):
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.lmain1.after(1, self.video_stream)

    def conclusion_wind(self):
        back = tk.Frame(width=self.screensize[0], height=self.screensize[1], bg='white')
        self.set_background_video()
        back.pack()

        self.set_text()
        self.set_graph()

    def set_background_video(self):
        self.cap1 = cv2.VideoCapture('videoplayback.mp4')
        self.lmain1 = tk.Label(root, text="hi")
        self.lmain1.pack(side="top")
        self.video_stream()


    def set_text(self):
        pass

    def set_graph(self):
        size_graph = plt.figure(figsize=(5, 5))
        result_graph = FigureCanvasTkAgg(size_graph, self)
        result_graph.get_tk_widget().pack(side="left")

        plt.plot([self.speed, self.volume])

        result_graph.draw()


root = tk.Tk()
app = Conclusion(master=root, speed=[23, 54, 6, 88, 34, 32, 5, 7], volume=[4,33,8,2,67,98,46,3])
app.mainloop()
