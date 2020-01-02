import curses
from curses import wrapper
from utilz import *
from random import randint
import time
from math import cos, sin, pi


# maxYX=stdWindow.getmaxyx()


class Screen:

    def __init__(self, scr):

        self.scr = scr
        self.maxYX = self.scr.getmaxyx()
        self.w = self.maxYX[1] - 1
        self.h = self.maxYX[0] - 1
        # self.w = 30
        # self.h = 20

        # characters
        self.v_bar = u"\u2502"
        self.h_bar = u"\u2504"
        self.cross = u"\u253C"
        self.p1 = "x"
        self.p2 = "o"

        # self.screen = [[None for x in range(self.w)] for y in range(self.h)]    #2d array to store image

        self.blank = " "

        self.initScreen()

        # self.screen[4][2] = "x"
        # self.screen[0][0] = "x"

        log("board width", self.w)
        log("board height", self.h)

        # log("screen", self.screen[9][4])

    # def updateScreen(self):
    #
    #     self.w = self.maxYX[1]
    #     self.h = self.maxYX[0]

    def initScreen(self):

        self.screen = [[self.blank for y in range(self.h)] for x in range(self.w)]

    def clearScreen(self):
        self.scr.clear()
        self.screen = [[self.blank for y in range(self.h)] for x in range(self.w)]

    def point(self, x, y):
        x, y, = int(x), int(y)
        self.screen[x][y] = "x"

    def set(self, x, y, c):
        if not x > self.w and not y > self.h and not x < 0 and not y < 0:
            self.screen[x][y] = c

    def line(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        signX = 1 if x1 < x2 else -1
        signY = 1 if y1 < y2 else -1

        error = dx - dy
        # self.screen[x2][y2] = "x"
        self.set(x2, y2, "x")
        while not x1 == x2 or not y1 == y2:
            # self.screen[x1][y1] = "x"
            self.set(x1, y1, "x")
            error2 = error * 2
            if error2 > -dy:
                error -= dy
                x1 += signX

            if error2 < dx:
                error += dx
                y1 += signY

    def centerLine(self, x, y, a, l):
        x, y, a, l = float(x), float(y), float(a), float(l)
        l *= 0.5
        x1 = x + cos(a) * l
        y1 = y - sin(a) * l
        x2 = x + cos(a + pi) * l
        y2 = y - sin(a + pi) * l
        self.line(x1, y1, x2, y2)

    def angleLine(self, x, y, a, l):

        x, y, a, l = float(x), float(y), float(a), float(l)
        self.line(x, y, x + cos(a) * l, y - sin(a) * l)
        self.point(x, y)
        self.point(x + cos(a) * l, y - sin(a) * l)

    def numScreen(self):
        log("numscreen")
        c = 0
        for y in range(self.h):
            for x in range(self.w):
                if c == 10:
                    c = 0
                self.screen[x][y] = str(c)
                c += 1

    def yScreen(self):
        for y in range(self.h):
            for x in range(self.w):
                # ys = -y+self.h-1
                self.screen[x][y] = str(y)

    def randomScreen(self):

        for y in range(self.h):
            for x in range(self.w):
                self.screen[x][y] = str(randint(0, 9))

    def cursesDisplay(self):
        self.scr.clear()
        # for x in range(self.w):
        #     for y in range(self.h):
        #         cell = self.screen[x][y]
        #         if cell is not None:
        #             self.scr.addch(y,x,cell)

        for y in range(self.h):
            for x in range(self.w):
                cell = self.screen[x][y]
                y = -y + self.h - 1
                self.scr.addch(y, x, cell)

    def simpleDisplay(self):

        for y in reversed(range(self.h)):
            for x in range(self.w):
                logNoString(self.screen[x][y])
            logNoString("\n")


def log(string, value=None):
    if value:
        item = (f"{string}: {value}\n")
    else:
        item = (f"{string}\n")

    with open('log.txt', 'a+') as output:

        output.write(item + "\n")


def logNoString(v):
    with open('log.txt', 'a+') as output:
        output.write(str(v))


if __name__ == "__main__":

    with open('log.txt', 'w+') as output:
        output.write("")


    def main(scr):
        scr.nodelay(1)
        board = Screen(scr)
        # board.line(0, 0, 5, 5)
        # board.yScreen()
        # board.numScreen()
        # board.randomScreen()
        # board.simpleDisplay()
        count = 0

        while True:
            sc = count * 0.05 / 2
            c = scr.getch()
            curses.flushinp()
            # scr.clear()
            board.clearScreen()

            # board.line(randint(0,board.w-1),randint(0,board.h-1),randint(0,board.w-1),randint(0,board.h-1))
            board.line(0, 1, 10, 10)
            board.set(-5, 5, "x")
            #board.angleLine(board.w / 2, board.h / 2, sc, 10)
            # board.point((sin(sc)*20+board.w/2), (cos(sc)*10+board.h/2)*1)
            board.centerLine(board.w/2,board.h/2, sc, 25)

            board.cursesDisplay()
            time.sleep(0.001)
            count += 1

wrapper(main)
