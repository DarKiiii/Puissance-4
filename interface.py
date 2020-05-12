# external modules // ----------NEED pillow installed-----------
from tkinter import *; import random; from PIL import Image, ImageTk;

# CONFIG
w, h = 1280, 720

# ---------- MODULES -----------
class Root:
    '''
    main tkinter window
    '''
    def __init__(self, w, h):
        self.tk = Tk()
        scrw, scrh = self.tk.winfo_screenwidth(), self.tk.winfo_screenheight();
        self.tk.title("Puissance 4")
        self.tk.geometry("%dx%d+%d+%d"%(w, h, scrw/2-w/2, scrh/2-h/2));
        self.tk.resizable(False, False)
        self.buts = {};

    def new_but(self, name, img, size, pos, onclick, args=()):
        self.buts[name] = ImgButton(self, img, size, pos, onclick, args);

    def destroy(self):
        self.tk.destroy()

    def mainloop(self):
        self.tk.mainloop()

class App:
    '''
    tkinter label that can be used as non direct parent for other widgets
    img     : path to image
    '''
    def __init__(self, master, img):
        self.master = master
        self.img = ImageTk.PhotoImage(Image.open(img).resize((w, h)), Image.ANTIALIAS);
        self.tk = Label(master.tk, image=self.img);
        self.tk.pack();
        self.buts = {};

    def new_but(self, name, img, size, pos, onclick, args=()):
        self.buts[name] = ImgButton(self, img, size, pos, onclick, args);

    def destroy(self):
        self.tk.destroy()
        del(self)

class ImgButton:
    '''
    create a button with a label
    img     : button image path
    onclick : function called on click
    size    : dictionary with real size of the image
    pos     : args for tk.place function
    '''
    def __init__(self, master, img, size, pos, onclick, args=()):
        self.master = master
        self.img = ImageTk.PhotoImage(Image.open(img).resize((round(size["w"]*(w/1920)), round(size["h"]*(h/1080))), Image.ANTIALIAS));
        self.tk = Label(master.tk, image=self.img, bd=0);
        self.tk.bind("<ButtonPress-1>", lambda event : onclick(*args));
        self.tk.place(pos);

    def destroy(self):
        self.tk.destroy();
        del(self)