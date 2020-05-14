# external modules // ----------NEED pillow installed-----------
from tkinter import *; import random; from PIL import Image, ImageTk;

# CONFIG
w, h = 1280, 720

def none():
    return None

def img_resize(img_name, size):
    img = Image.open(img_name);
    width, height = img.size;
    if size["w"] and size["h"]:
        resized_img = img.resize((size["w"], size["h"]));
    elif size["w"]:
        resized_img = img.resize((size["w"], round(height*(size["w"]/width))));
    elif size["h"]:
        resized_img = img.resize((round(width*(size["h"]/height)), size["h"]));
    else:
        print("error appened while resizing", img_name, "image")
    return ImageTk.PhotoImage(resized_img, Image.ANTIALIAS);

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

    def new_but(self, name, img, size, pos, onclick=none, args=()):
        self.buts[name] = ImgButton(self, img, size, pos, onclick, args);

    def lift_widgets(self):
        for k, w in self.buts.items():
            w.tk.lift()

    def destroy(self):
        self.tk.destroy()

    def mainloop(self):
        self.tk.mainloop()

class App:
    '''
    tkinter label that can be used as direct parent for other widgets
    img     : path to image
    '''
    def __init__(self, master, img):
        self.master = master
        self.img = ImageTk.PhotoImage(Image.open(img).resize((w, h)), Image.ANTIALIAS);
        self.tk = Label(master.tk, image=self.img);
        self.tk.pack();
        self.buts = {};
        self.entry = {};

    def new_but(self, name, img, size, pos, onclick=none, args=()):
        self.buts[name] = ImgButton(self, img, size, pos, onclick, args);

    def new_entry(self, name, size, pos, font=("Helvetica",10), bg='#FFF', default=""):
        self.entry[name] = TxtInput(self, size, pos, font, bg, default);

    def lift_widgets(self):
        for k, w in self.buts.items():
            w.tk.lift();
        for k, w in self.entry.items():
            w.tk.lift();
        self.master.lift_widgets()

    # def destroy_buts( self ):
    #     button = self.buts["color"]
    #     button.tk.destroy();
    #     if self.color == "red":
    #         self.new_but( "color", "color_yel.png", {"w" :250, "h" :50}, {"anchor" :N, "relx" :0.515, "rely" :0.522},self.destroy_buts );
    #         self.color = "yel"
    #     else:
    #         self.new_but( "color", "color_red.png", {"w" :250, "h" :50}, {"anchor" :N, "relx" :0.515, "rely" :0.522},self.destroy_buts );
    #         self.color = "red";

    def destroy(self):
        self.tk.destroy();
        del(self);

class ImgButton:
    '''
    create a button with a label
    img     : button image path
    onclick : function called on click
    size    : dictionary with real size of the image
    pos     : args for tk.place function
    '''
    def __init__(self, master, img, size, pos, onclick=none, args=()):
        self.master = master;
        self.img = img_resize(img, size)
        self.tk = Label(master.tk, image=self.img, bd=0);
        self.tk.bind("<ButtonPress-1>", lambda event : onclick(*args));
        self.tk.place(pos);

    def destroy(self):
        self.tk.destroy();
        del(self);


class TxtInput:

    def __init__(self, master, size, pos, font=("Helvetica",10), bg='#FFF', default=""):
        self.master = master;
        self.txtvar = StringVar();
        self.txtvar.set(default);
        self.tk = Entry(master.tk, bd=0, bg=bg, width=size["w"], font=font, textvariable=self.txtvar);
        self.tk.place(pos);

    def destroy(self):
        self.tk.destroy();
        del(self);
