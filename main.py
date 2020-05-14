'''
------------WARNING : Tkinter interface needs 'pillow' (PIL) installed to work--------------
'''
from grid import *; from interface import *;

# {"w" :round($$*(w/1920)), "h" :round($$*(h/1080))} ## sample for buttons size
main_but_size = {"w" :round(474*(w/1920)), "h" :round(134*(h/1080))};

class Game():
    '''
    the game
    '''
    def __init__( self ):
        self.root = Root(w,h);
        self.root.new_but( "close", "close_button.png", {"w" :36, "h" :36}, {"anchor" :NE, "x" :w, "y" :0}, self.root.destroy);
        self.menu = None
        self.main_menu();

    def main_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu=App( self.root, "menu.png" );
        self.menu.new_but( "solo", "solo_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.4}, self.solo_menu );
        self.menu.new_but( "multi", "multi_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.55},  print );
        self.menu.new_but( "rules", "rules_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.rules_menu );
        self.menu.lift_widgets();
        self.menu.tk.mainloop();

    def rules_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu=App( self.root, "bg.png" );
        self.menu.new_but('rules_png',"rules.png", {"w" :round(1869*(w/1920)), "h" :round(693*(h/1080))}, {"anchor" :N, "relx" :0.5, "rely" :0.1})
        self.menu.new_but( "rules", "menu_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.main_menu );
        self.menu.lift_widgets();
        self.menu.tk.mainloop();


    def solo_menu( self ):
        if self.menu :
            self.menu.destroy();
        self.menu=App( self.root, "solo-bg.png" );
        self.menu.new_entry("playername", {"w" :14},{"relx" :0.4125, "rely" :0.405}, ("Helvetica",27), "#400000", "Nom du joueur");
        # self.menu.new_but("color","color_red.png",{"w" :250, "h" :50}, {"anchor" :N, "relx" :0.515, "rely" :0.522},self.menu.destroy_buts)
        self.menu.new_but( "start", "start_button.png", main_but_size, {"anchor" :N, "relx" :0.49, "rely" :0.73},print )
        self.menu.new_but( "back", "back_button.png", {"w" :round(166*(w/1920)), "h" :round(134*(h/1080))}, {"anchor" :N, "relx" :0.05, "rely" :0.05},self.main_menu )
        self.menu.lift_widgets();
        self.menu.tk.mainloop();

if __name__ == '__main__':
    game = Game();
