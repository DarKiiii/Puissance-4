'''
------------WARNING : Tkinter interface needs 'pillow' (PIL) installed to work--------------
'''
from grid import *; from interface import *;

class Game():
    '''
    the game
    '''
    def __init__( self ):
        self.root = Root(w,h);
        self.root.new_but( "close", "close_button.png", {"w" :54, "h" :54}, {"anchor" :NE, "x" :w, "y" :0}, self.root.destroy);
        self.menu = None
        self.main_menu();

    def main_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu=App( self.root, "menu.png" );
        self.menu.new_but( "solo", "solo_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.4}, self.menu_solo );
        self.menu.new_but( "multi", "multi_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.55},  print );
        self.menu.new_but( "rules", "rules_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.rules_menu );
        self.root.buts["close"].tk.lift()
        self.menu.tk.mainloop();

    def rules_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu=App( self.root, "bg.png" );
        self.menu.new_but('rules_png',"rules.png", {"w" :1869, "h" :693}, {"anchor" :N, "relx" :0.5, "rely" :0.1},print)
        self.menu.new_but( "rules", "menu_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.main_menu );
        self.root.buts["close"].tk.lift()
        self.menu.tk.mainloop();


    def menu_solo( self ):
        if self.menu :
            self.menu.destroy();
        self.menu=App( self.root, "font-solo.png" );
        self.menu.new_text("Pseudo",{"w" :250, "h" :50},{"x" :0.5, "y" :0.73});
        self.menu.new_but("color","color_red.png",{"w" :250, "h" :50}, {"anchor" :N, "relx" :0.515, "rely" :0.522},self.menu.destroy_buts)
        self.menu.new_but( "start", "start_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.49, "rely" :0.73},print )
        self.menu.new_but( "back", "back_button.png", {"w" :166, "h" :134}, {"anchor" :N, "relx" :0.05, "rely" :0.05},self.main_menu )
        self.menu.tk.mainloop();





if __name__ == '__main__':
    game = Game();
