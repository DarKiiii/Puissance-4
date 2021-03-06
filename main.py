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
        self.menu.new_but( "multi", "multi_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.55}, self.multi_menu );
        self.menu.new_but( "rules", "rules_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.rules_menu );
        self.menu.lift_widgets();
        self.menu.tk.mainloop();

    def rules_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu=App( self.root, "bg.png" );
        self.menu.new_but("rules_png","rules.png", {"w" :round(1869*(w/1920)), "h" :round(693*(h/1080))}, {"anchor" :N, "relx" :0.5, "rely" :0.1})
        self.menu.new_but( "menu", "menu_button.png", main_but_size, {"anchor" :N, "relx" :0.5, "rely" :0.73}, self.main_menu );
        self.menu.lift_widgets();
        self.menu.tk.mainloop();


    def solo_menu( self ):
        if self.menu :
            self.menu.destroy();
        self.menu=App( self.root, "solo-bg.png" );
        self.menu.new_entry("playername", {"w" :14},{"relx" :0.4125, "rely" :0.405}, ("Helvetica",27), "#400000", "Nom du joueur");
        self.menu.new_switch("color", ("color_red.png", "color_yel.png"), {"w" :round(333*(w/1920)), "h" :round(58*(h/1080))}, {"relx" :0.45, "rely" :0.514}, vars=("red", "yel"))
        self.menu.new_switch("difficulté",("SWITCH_FACILE.png","SWITCH_DIFFICILE.png"),{"w" :round(222*(w/1920)), "h" :round(68*(h/1080))}, {"relx" :0.49, "rely" :0.599}, vars=("dif", "ez"))
        self.menu.new_but("start", "start_button.png", main_but_size, {"anchor" :N, "relx" :0.49, "rely" :0.73})
        self.menu.new_but("back", "back_button.png", {"w" :round(166*(w/1920)), "h" :round(134*(h/1080))}, {"anchor" :N, "relx" :0.05, "rely" :0.05}, self.main_menu)
        self.menu.lift_widgets();
        self.menu.tk.mainloop();

    def multi_menu( self ):
        if self.menu:
            self.menu.destroy();
        self.menu =  App(self.root,'fond-multi.png');
        self.menu.new_but( "back", "back_button.png", {"w" :round( 166 * (w / 1920) ), "h" :round( 134 * (h / 1080) )},{"anchor" :N, "relx" :0.05, "rely" :0.05}, self.main_menu );
        self.menu.new_switch( "difficulté", ("SWITCH_FACILE.png", "SWITCH_DIFFICILE.png"),{"w" :round( 222 * (w / 1920) ), "h" :round( 68 * (h / 1080) )},{"relx" :0.7255, "rely" :0.49}, vars=("dif", "ez") );
        self.menu.new_entry("playername_red",{"w" :14},{"relx" :0.21, "rely" :0.68}, ("Helvetica",27), "#400000", "Nom du joueur 1");
        self.menu.new_entry( "playername_yel", {"w" :14}, {"relx" :0.21, "rely" :0.545}, ("Helvetica", 27), "#400000","Nom du joueur 2" );
        self.menu.new_but( "start", "start_button.png", main_but_size, {"anchor" :N, "relx" :0.72, "rely" :0.73},self.game_duo);
        self.menu.lift_widgets();
        self.menu.tk.mainloop();

    def game_duo( self ):
        if self.menu:
            settings = self.menu.get_setting()
            if settings["playername_red"] == None or settings["playername_yel"] == None:
                return
            print(settings)
            self.menu.destroy();
        self.menu = App(self.root,'bg-jeux.png');
        self.menu.new_but("grille","grille.png", {"w" :round( 1046 * (w / 1920) ), "h" :round( 852 * (h / 1080) )},{"anchor" :N, "relx" :0.5, "rely" :0.2},print);
        self.menu.new_but( "f1", "fleche blue.png", {"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.266, "rely" :0.06},print);
        self.menu.new_but( "f2", "fleche blue.png",{"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.345, "rely" :0.06}, print ) ;
        self.menu.new_but( "f3", "fleche blue.png",{"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.424, "rely" :0.06}, print ) ;
        self.menu.new_but( "f4", "fleche blue.png",{"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.503, "rely" :0.06}, print ) ;
        self.menu.new_but( "f5", "fleche blue.png",{"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.582, "rely" :0.06}, print ) ;
        self.menu.new_but( "f6", "fleche blue.png",{"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.661, "rely" :0.06}, print ) ;
        self.menu.new_but( "f7", "fleche blue.png", {"w" :round( 138 * (w / 1920) ), "h" :round( 150 * (h / 1080) )},{"anchor" :N, "relx" :0.740, "rely" :0.06}, print ) ;
        self.menu.new_but( "pred", "perso-red.png", {"w" :round( 407 * (w / 1920) ), "h" :round( 532 * (h / 1080) )},
                           {"anchor" :N, "relx" :0.9, "rely" :0.3}, print ) ;
        self.menu.new_but( "pyel", "perso-yel.png", {"w" :round( 407 * (w / 1920) ), "h" :round( 532 * (h / 1080) )},
                           {"anchor" :N, "relx" :0.1, "rely" :0.3}, print ) ;
        self.menu.texte("playername_red_name",{"w" :14},{"relx" :0.21, "rely" :0.68}, ("Helvetica",27), "#400000", settings["playername_red"])
        self.menu.lift_widgets();
        self.menu.tk.mainloop();






if __name__ == '__main__':
    game = Game();
