import curses
from curses import wrapper

# maxYX=stdWindow.getmaxyx()


class Board:

    def __init__(self, board_width = 3, board_height = 3):

        self.board_width = board_width      # board as in actual squares the user can choose from
        self.board_height = board_height
        self.w = (self.board_width)*2+1     # width of the display in characters, including grid characters
        self.h = (self.board_height)*2+1

        self.v_bar = u"\u2502"

        self.h_bar = u"\u2504"
        self.cross = u"\u253C"
        self.p1 = "x"
        self.p2 = "o"

        #screen = [["{},{}".format(y,x) for x in range(w)] for y in range(h)]
        #
        # screen = [[None for x in range(w)] for y in range(h)]

        self.screen = [[None for x in range(self.w)] for y in range(self.h)]
        self.drawGrid()

    def drawGrid(self):

        for i in range(self.w):
            if i % 2 == 0:
                self.vLine(0, i, self.h)

        for i in range(self.h):
            if i % 2 == 0:
                self.hLine(i, 0, self.w)


    def simpleDisplay(self):

        for y in range(self.h):
            for x in range(self.w):
                z = self.screen[y][x]
                if z is None:
                    char = "n"
                else:
                    char = z
                print(char, end = "")

            print("")

    def cursesDisplay(self, scr):

        for y in range(self.h):
            for x in range(self.w):
                cell = self.screen[y][x]
                if cell is not None:
                    scr.addch(y,x,cell)


    # def getBoard(self):
    #     return self.screen

    def hLine(self,y,x,l):
        for i in range(l):

            if self.screen[y][x+i] == self.v_bar:
                self.screen[y][x + i] = self.cross
            else:
                self.screen[y][x+i] = self.h_bar


    def vLine(self,y,x,l):
        for i in range(l):
            if self.screen[y + i][x] == self.h_bar:
                self.screen[y + i][x]  = self.cross
            else:
                self.screen[y+i][x] = self.v_bar


    def p1_piece(self,y,x):
        if self.screen[y][x] == " ":
            self.screen[y][x] = self.p1
        else:
            raise Exception('space not empty')


    def p2_piece(self,y,x):
        if self.screen[y][x] == " ":
            self.screen[y][x] = self.p2
        else:
            raise Exception('space not empty')

#
# board = Board()
#
# board.drawGrid()
#
# board.simpleDisplay()
#

if __name__ == "__main__":
    board = Board()
    board.drawGrid()
    board.simpleDisplay()