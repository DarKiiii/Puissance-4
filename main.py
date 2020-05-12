'''
------------WARNING : Tkinter interface needs 'pillow' (PIL) installed to work--------------
'''
from grid import *; from interface import *;

class Game():
    '''
    the game
    '''
    def __init__( self ):
        self.root = Root(w,h)
        self.menu()
        self.root.new_but( "close", "close_button.png", {"w" :54, "h" :54}, {"anchor" :NE, "x" :w, "y" :0}, self.root.destroy)

    def menu( self ):
        self.menu=App( self.root, "menu.png" );
        self.menu.new_but( "solo", "solo_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.4}, print )
        self.menu.new_but( "multi", "multi_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.55},  print )
        self.menu.new_but( "rules", "rules_button.png", {"w" :474, "h" :134}, {"anchor" :N, "relx" :0.5, "rely" :0.73}, print )
        self.menu.tk.mainloop()

    def rules( self ):
        print("")


    # def menu_solo( self ):
    #     print("cccc")




if __name__ == '__main__':
    game = Game();
