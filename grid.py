class Grid:
    '''
    grille de puissance 4 toute simple
    '''
    def __init__ (self):
        self.content = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    def print (self):
        '''
        fonction de développement
        affiche la grille dans la console
        '''
        for i in self.content:
            str = ""
            for j in i:
                if j == 1:
                    str += " R"
                elif j == -1:
                    str += " J"
                else:
                    str += " O"
            print(str)

    def win (self, p):
        global hasWin
        '''
        est appellé si un joueur a gagné
        '''
        print(p, "a gagné")
        hasWin = p


    def check (self):
        '''
        vérifie si un joueur à gagné
        '''
        for y in range(6):
            for x in range(7):
                if x < 4 and y < 3:
                    if self.content[y][x] + self.content[y+1][x+1] + self.content[y+2][x+2] + self.content[y+3][x+3] == 4:
                        self.win(1)
                        return
                    elif self.content[y][x] + self.content[y+1][x+1] + self.content[y+2][x+2] + self.content[y+3][x+3] == -4:
                        self.win(-1)
                        return
                if y < 3:
                    if self.content[y][x] + self.content[y+1][x] + self.content[y+2][x] + self.content[y+3][x] == 4:
                        self.win(1)
                        return
                    elif self.content[y][x] + self.content[y+1][x] + self.content[y+2][x] + self.content[y+3][x] == -4:
                        self.win(-1)
                        return
                if x < 4:
                    if self.content[y][x] + self.content[y][x+1] + self.content[y][x+2] + self.content[y][x+3] == 4:
                        self.win(1)
                        return
                    elif self.content[y][x] + self.content[y][x+1] + self.content[y][x+2] + self.content[y][x+3] == -4:
                        self.win(-1)
                        return
        return False

    def add (self, p, x):
        '''
        p : player number
        x : id of case in inner list
        y : id of case in outter list
        '''
        y = 0
        while  y < 6 and self.content[y][x] == 0:
            y += 1
        self.content[y-1][x] = p
        self.check()