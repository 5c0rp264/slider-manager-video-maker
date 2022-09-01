from tkinter import *
from videoReader import launch_video
from PIL import ImageTk, Image
from time import sleep
from os import path

class Slideshow(Tk):
    def __init__(self, slide_data):
        Tk.__init__(self)
        self.geometry("1920x1080")
        self.attributes("-fullscreen", True)
        self.configure(background='black')
        self.config(cursor="none")
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.medias = [val["filename"] for val in slide_data]
        self.durations = [val["duration"] for val in slide_data]
        self.track_media_index = 0
        self.media_canvas = Canvas(self, width = self.w, height = self.h, bg='black', highlightthickness=0)
        self.media_canvas.pack()


    def show_slides(self):
        if self.track_media_index < len(self.medias):     
            # TODO :  test if media is image or video and launch adaptatively 
            current_slide = self.medias[self.track_media_index]
            self.track_media_index +=1
            pil_img = Image.open(path.join('output/', current_slide))
            img = ImageTk.PhotoImage(pil_img)            
            resize_ratio = min(self.w/pil_img.size[0], self.h/pil_img.size[1])
            resized_slide = pil_img.resize((int(pil_img.size[0]*resize_ratio), int(pil_img.size[1]*resize_ratio)), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(resized_slide)
            self.media_canvas.create_image(int(self.w/2), 0, anchor=N, image=img)
            self.media_canvas.current = img
            self.after(self.durations[self.track_media_index - 1]*1000, self.show_slides)
        else:
            self.track_media_index = 0
            self.show_slides()

