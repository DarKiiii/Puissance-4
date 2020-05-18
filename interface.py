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
        self.widgets = {};

    def new_but(self, name, img, size, pos, onclick=none, args=()):
        self.widgets[name] = ImgButton(self, img, size, pos, onclick, args);

    def lift_widgets(self):
        for k, w in self.widgets.items():
            w.tk.lift();

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
        self.widgets = {};
        self.widgets_info = {};

    def new_but(self, name, img, size, pos, onclick=none, args=()):
        self.widgets[name] = ImgButton(self, img, size, pos, onclick, args);

    def new_entry(self, name, size, pos, font=("Helvetica",10), bg='#FFF', default=""):
        self.widgets[name] = TxtInput(self,name, size, pos, font, bg, default);
        self.widgets_info[name]= None

    def new_switch(self, name, img, size, pos, onclick=none, args=(), default=0, vars=()):
        self.widgets[name] = Switch(self, img,name, size, pos, onclick, args, default, vars);
        self.widgets_info[name] = 0

    def get_setting( self ):
        return self.widgets_info

    def set_setting( self,var,name):
        self.widgets_info[name] = var

    def lift_widgets(self):
        for k, w in self.widgets.items():
            w.tk.lift();
        self.master.lift_widgets()


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

    def __init__(self, master,name, size, pos, font=("Helvetica",10), bg='#FFF', default=""):
        self.name = name
        self.master = master;
        self.txtvar = StringVar();
        self.txtvar.set(default);
        self.tk = Entry(master.tk, bd=0, bg=bg, width=size["w"], font=font, textvariable=self.txtvar);
        self.tk.bind( "<KeyRelease>", lambda event :self.clicked() ) ;
        self.tk.place(pos);

    def destroy(self):
        self.tk.destroy();
        del(self);

    def clicked( self ):
        var = self.tk.get()
        self.master.set_setting(var,self.name)

class Switch:

    def __init__(self, master,imgs,name, size, pos, onclick=none, args=(), default=0, vars=()):
        self.master = master;
        self.name = name
        self.imgs = []
        for img in imgs:
            self.imgs.append(img_resize(img, size))
        self.var = default
        self.cmd = onclick
        self.args = args
        self.vars = vars
        self.tk = Label(master.tk, image=self.imgs[self.var], bd=0);
        self.tk.bind("<ButtonPress-1>", lambda event : self.clicked());
        self.tk.place(pos);

    def clicked(self):
        self.cmd(*self.args);
        self.var += 1;
        if self.var >= len(self.imgs) or self.var >= len(self.vars):
            self.var = 0;
        self.master.set_setting(self.var,self.name);
        self.tk.configure(image=self.imgs[self.var]);
        self.master.lift_widgets();

    def destroy(self):
        self.tk.destroy();
        del(self);


