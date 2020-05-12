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
        self.menu.new_but( "solo", "solo_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.4}, print );
        self.menu.new_but( "multi", "multi_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.55},  print );
        self.menu.new_but( "rules", "rules_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.rules_menu );
        self.root.buts["close"].tk.lift()
        self.menu.tk.mainloop();

    def rules_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu=App( self.root, "bg.png" );
        self.menu.new_but( "rules", "rules_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.main_menu );
        self.root.buts["close"].tk.lift()
        self.menu.tk.mainloop();


    # def menu_solo( self ):
    #     print("cccc")


if __name__ == '__main__':
    game = Game();
