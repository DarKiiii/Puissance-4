'''
------------WARNING : Tkinter interface needs 'pillow' (PIL) installed to work--------------
'''
from grid import *; from interface import *;

class Game():

    def __init__(self):
        self.root = Root(w,h)
        self.root.new_but( "close", "close_button.png", self.root.destroy, {"w" :54, "h" :54},{"anchor" :NE, "x" :w, "y" :0} )
        self.menu()


    def menu( self ):
        self.menu=App( self.root, "menu.png" );
        self.menu.new_but( "solo", "solo_button.png",print, {"w" :474, "h" :134},{"anchor" :N, "relx" :0.5, "rely" :0.4} )
        self.menu.new_but( "multi", "multi_button.png", print, {"w" :474, "h" :134},{"anchor" :N, "relx" :0.5, "rely" :0.55} )
        self.menu.new_but( "rules", "rules_button.png", print, {"w" :474, "h" :134},{"anchor" :N, "relx" :0.5, "rely" :0.73} )
        self.mainloop()

    def menu_solo( self ):
        print("cccc")


    def mainloop( self ):
        self.root.mainloop()


if __name__ == '__main__':
    game = Game()