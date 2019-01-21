import cv2
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from eventlet.green import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Conclusion(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        # self.x([23, 54, 6, 88, 34, 32, 5, 7])

    def create_widgets(self):

        self.cap1 = cv2.VideoCapture('videoplayback.mp4')
        self.lmain1 = tk.Label(root, text="hi")
        self.lmain1.pack()
        self.init_canvas()
        self.x([23, 54, 6, 88, 34, 32, 5, 7])

        self.video_stream()


    def init_canvas(self):
        import ctypes
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        back = tk.Frame(width=screensize[0], height=screensize[1], bg='white')
        back.pack()
        # self.vid = MyVideoCapture(video_source)
        # self.vid = cv2.VideoCapture('mySong.mp4')
        # self.vid.isOpened()
        # video_source = 'mySong.mp4'
        # window_title = "Tkinter and OpenCV"
        # self.window# = window
        # self.window.title(window_title)
        # self.video_source = video_source
        #
        # # open video source (by default this will try to open the computer webcam)
        # self.vid = MyVideoCapture(self.video_source)
        #
        # # Create a canvas that can fit the above video source size
        # self.canvas = tkinter.Canvas(window, width=self.vid.width, height=self.vid.height)
        # self.canvas.pack()
        #
        # # Button that lets the user take a snapshot
        # self.btn_snapshot = tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        # self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        #
        # # After it is called once, the update method will be automatically called every delay milliseconds
        # self.delay = 15
        # self.update()
        # self.window.mainloop()

        # self.window = window
        #
        #
        # self.window.title(window_title)
        #
        # self.window.mainloop()

    def video_stream(self):
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.lmain1.after(1, self.video_stream)

    def x(self, speed):
        self.f1 = plt.figure(figsize=(5, 5))
        self.canvas1 = FigureCanvasTkAgg(self.f1, self)
        self.canvas1.get_tk_widget().pack(side="left")

        plt.plot(speed, speed)
        self.canvas1.draw()
        self.canvas1.draw()

        self.f2 = plt.figure(figsize=(5, 5))
        self.canvas2 = FigureCanvasTkAgg(self.f2, self)
        self.canvas2.get_tk_widget().pack(side="right")

        plt.plot(speed)
        self.canvas2.draw()

        # self.video_stream()
        # self.f = plt.figure(figsize=(5, 5))
        # self.canvas = FigureCanvasTkAgg(self.f, self)
        # self.canvas.get_tk_widget().pack(side="left")
        #
        # a = plt.plot(speed)
        # self.canvas.draw()
        #
        # b = plt.plot(speed[3:6])
        # self.canvas.draw()
    def set_back(self):
        pass

    def set_wind(self):
        # set frame

        # write sucsess
        pass

    def set_graph(self):
        pass


root = tk.Tk()
app = Conclusion(master=root)
app.mainloop()
