import ctypes
from PIL import ImageTk, Image
import cv2
import tkinter as tk
import music_control
import speed_detection
import threading
import last_screen
import os

class ImageWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()


        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        File = os.listdir('images_collection/')
        lf = []
        for i in range(9):
            lf.append('images_collection/' + File[1])
            # img = ImageTk.PhotoImage(Image.open(FileDir))
        # a = "C:\\Users\\שרה ויסברגר\\Desktop\\EXELLENTIM\\excellenteam-hackathon-ella-songo\\fa.png"
        # lf = [a, a, a, a, a, a, a, a, a]

        # print(lf)
        imgee = last_screen.last_screen(lf)
        img = tk.PhotoImage(imgee)
        panel = tk.Label(self, text="image pro")
        panel.image = img
        panel.grid()







