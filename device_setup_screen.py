from tkinter import *
from videoReader import launch_video
from PIL import ImageTk, Image
from time import sleep
from os import path

class Device_setup_screen(Tk):
    def __init__(self, uid=None, message=None):
        Tk.__init__(self)
        self.geometry("1920x1080")
        self.attributes("-fullscreen", True)
        self.configure(background='#aec6f5')
        self.config(cursor="none")
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.canvas = Canvas(self, width = self.w, height = self.h, bg='#aec6f5', highlightthickness=0)
        
        # Add up a qr code to contact us
        pil_img = Image.open('static/qr_contact.png')
        img = ImageTk.PhotoImage(pil_img)            
        resize_ratio = min((self.w/4)/pil_img.size[0], (self.h/2)/pil_img.size[1])
        resized_img = pil_img.resize((int(pil_img.size[0]*resize_ratio), int(pil_img.size[1]*resize_ratio)), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized_img)
        self.canvas.create_image(int(self.w*0.75), int(self.h*0.05), anchor='n', image=img)
        self.canvas.currentImg = img
        self.canvas.create_text(int(self.w*0.75), int(self.h*0.52), text="https://slider-manager.s-corp.it/contactus", fill="black", font=('Helvetica 20 bold'), anchor='n')

        # Create a black rectangle on the left part of the screen
        self.canvas.create_rectangle(0, 0, int(self.w*0.5), int(self.h),outline="#555555", fill="#555555")
        # Add up text to explain the process to the client
        
        if uid is not None:
            self.canvas.create_text(int(self.w*0.05), int(self.h*0.35), text="Votre code :", fill="white", font=('Helvetica 45 bold'), anchor='w')
            self.canvas.create_text(int(self.w*0.05), int(self.h*0.42), text=uid, fill="white", font=('Helvetica 45'), anchor='w')
            
            self.canvas.create_text(int(self.w*0.05), int(self.h*0.6), text="Merci de nous contacter avec le code ci-dessus afin\nde finir le paramétrage de votre appareil à distance", fill="white", font=('Helvetica 25'), anchor='w')
        elif message is not None:
            self.canvas.create_text(int(self.w*0.1), int(self.h*0.45), text=message, fill="white", font=('Helvetica 20 bold'), anchor='w')
        points = [int(self.w*0.5), int(self.h*1), int(self.w*1), int(self.h*0.5), int(self.w*1), int(self.h*1)]
        self.canvas.create_polygon(points, fill='#002366')
        self.canvas.create_text(int(self.w*0.95), int(self.h*0.9), text="Contactez nous !", fill="white", font=('Helvetica 45 bold'), anchor='e')

        self.canvas.pack()
