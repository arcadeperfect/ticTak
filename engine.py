import curses
from curses import wrapper
# from utilz import *
from random import randint
import time
from math import cos, sin, pi
import scipy
from threedee import *

# maxYX=stdWindow.getmaxyx()


class Screen(object):

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

    def set(self, x, y, c = "*"):

        # x = int((x-self.w/2) * 1.5 +(self.w/2))
        x, y  = int(x), int(y)
        if not x > self.w-1 and not y > self.h-1 and not x < 0 and not y < 0:
            self.screen[x][y] = c

    def line(self, x1, y1, x2, y2):
        s = 2
        x1 = x1 *s - self.w/s
        x2 = x2 *s - self.w/s
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

    def center_line(self, x, y, a, l):  # x, y, angle, length
        x, y, a, l = float(x), float(y), float(a), float(l)
        l *= 0.5
        x1 = x + cos(a) * l
        y1 = y - sin(a) * l
        x2 = x + cos(a + pi) * l
        y2 = y - sin(a + pi) * l
        self.line(x1, y1, x2, y2)

    def center_v_line(self, x, y, l):   # vertical line from center
        self.center_line(x, y, pi / 2, l)

    def center_h_line(self, x, y, l):   # horizontal line from center
        self.center_line(x, y, pi * 2, l)

    def angle_line(self, x, y, a, l):   # define line by one point + angle + length

        x, y, a, l = float(x), float(y), float(a), float(l)
        self.line(x, y, x + cos(a) * l, y - sin(a) * l)
        self.point(x, y)
        self.point(x + cos(a) * l, y - sin(a) * l)

    def num_screen(self):
        log("numscreen")
        c = 0
        for y in range(self.h):
            for x in range(self.w):
                if c == 10:
                    c = 0
                self.screen[x][y] = str(c)
                c += 1

    def y_screen(self):
        for y in range(self.h):
            for x in range(self.w):
                # ys = -y+self.h-1
                self.screen[x][y] = str(y)

    def random_screen(self):

        for y in range(self.h):
            for x in range(self.w):
                self.screen[x][y] = str(randint(0, 9))

    def curses_display(self):   # display the array through curses
        self.scr.clear()

        for y in range(self.h):
            for x in range(self.w):
                cell = self.screen[x][y]
                y = -y + self.h - 1
                self.scr.addch(y, x, cell)

    def simple_display(self):   # write the display to text file

        for y in reversed(range(self.h)):
            for x in range(self.w):
                logNoString(self.screen[x][y])
            logNoString("\n")

    # def draw_cross(self, board):
    #
    #     cw = self.w / 2
    #     ch = self.h / 2
    #
    #     n = board.n
    #     x = board.x if board.x else cw
    #     y = board.y if board.y else ch
    #
    #     for i in range(n):
    #         self.center_v_line(x - 6, y, 20)
    #         # self.center_v_line(x - 12, y, 20)
    #         self.center_v_line(x + 6, y, 20)
    #         # self.center_v_line(x + 12, y, 20)
    #
    #         self.center_h_line(x, y - 3, 40)
    #         # self.center_h_line(x, y-8, 40)
    #         self.center_h_line(x, y + 3, 40)
    #         # self.center_h_line(x, y+8, 40)
    #         # self.center_v_line(cw - 2, x, 10)
    #         # self.center_v_line(cw - 4, x, 10)
    #         # self.center_v_line(cw + 2, x, 10)
    #         # self.center_v_line(cw + 4, x, 10)


# class GameBoard(object):
#
#     def __init__(self, n, x=None, y=None):
#         self.n = n
#         self.x = x
#         self.y = y
#         self.playerSpace = [[None for y in range(self.n)] for x in range(self.n)]
#
#     def set_player_1(self, x, y):
#         if self.playerSpace[x][y] is None:
#             self.playerSpace[x][y] = 1
#         else:
#             print("space not empty")
#
#     def set_player_2(self, x, y):
#         if self.playerSpace[x][y] is None:
#             self.playerSpace[x][y] = 2
#         else:
#             print("space not empty")

class Box(object):

    def __init__(self, n, x, y, screen):
        self.n = n
        self.x = x
        self.y = y
        self.screen = screen
        w = 4
        h = 2

        self.v1 = Line(x - w, y - h, x - w, y + h, self.screen)
        self.v2 = Line(x + w, y - h, x + w, y + h, self.screen)
        self.h1 = Line(x - w, y - h, x + w, y - h, self.screen)
        self.h2 = Line(x - w, y + h, x + w, y + h, self.screen)

    def draw(self):
        self.v1.draw()
        self.v2.draw()
        self.h1.draw()
        self.h2.draw()


class Grid(object):

    def __init__(self, n, x, y, screen):
        self.n = n
        self.x = x
        self.y = y
        self.screen = screen
        s = 1
        w = 6
        h = 6
        w *= s
        h *= s

        u = (2 + 1 / 3)

        self.v1 = Line(x - w, y - h * u, x - w, y + h * u, self.screen)
        self.v2 = Line(x + w, y - h * u, x + w, y + h * u, self.screen)
        self.h1 = Line(x - w * u, y - h, x + w * u, y - h, self.screen)
        self.h2 = Line(x - w * u, y + h, x + w * u, y + h, self.screen)


    #
    # def translate(self):


    def draw(self):
        self.v1.draw()
        self.v2.draw()
        self.h1.draw()
        self.h2.draw()

    def rotate(self, ergle):

        x = self.x
        y = self.y
        self.v1.rotate(ergle, x, y)
        self.v2.rotate(ergle, x, y)
        self.h1.rotate(ergle, x, y)
        self.h2.rotate(ergle, x, y)

    def translate(self, x,y):
        log("x", x)
        self.v1.translate(x,y)
        self.v2.translate(x,y)
        self.h1.translate(x,y)
        self.h2.translate(x,y)

    def scale(self, sx, sy = None):
        sy = sx if sy is None else sy
        self.v1.scale(sx,sy, self.x, self.y)
        self.v2.scale(sx,sy, self.x, self.y)
        self.h1.scale(sx,sy, self.x, self.y)
        self.h2.scale(sx,sy, self.x, self.y)


class Line(object):

    def __init__(self, x1, y1, x2, y2, screen):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.screen = screen
    #     self.get_pivot()
    #
    # def get_pivot(self):
    #     self.pivotX = (self.x1 + self.x2) / 2
    #     self.pivotY = (self.y1 + self.y2) / 2

    def translate(self, x, y):
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y

    def scale(self, sx, sy, px ,py):

        self.x1 = (self.x1 - px) * sx + px
        self.y1 = (self.y1 - py) * sy + py
        self.x2 = (self.x2 - px) * sx + px
        self.y2 = (self.y2 - py) * sy + py

    def rotate(self, angle, cx, cy):


        # log("x1", self.x1)
        self.x1, self.y1 = rotatePoint(angle, self.x1, self.y1, cx, cy)
        self.x2, self.y2 = rotatePoint(angle, self.x2, self.y2, cx, cy)
        # log("x1", self.x1)
        # logNoString("\n")

        '''angle = (angle ) * (Math.PI/180); // Convert to radians

        var rotatedX = Math.cos(angle) * (point.x - center.x) - Math.sin(angle) * (point.y-center.y) + center.x;

        var rotatedY = Math.sin(angle) * (point.x - center.x) + Math.cos(angle) * (point.y - center.y) + center.y;



        return new createjs.Point(rotatedX,rotatedY);'''

    def draw(self):
        self.screen.line(self.x1, self.y1, self.x2, self.y2)



class CenterLine(object):

    def __init__(self, x, y, a, l):
        self.x = x
        self.y = y
        self.a = a
        self.l = l
    def translate(self, x, y):
        self.x += x
        self.y += y
    def scale(self, s):
        self.l += s

    def rotate(self, r):
        self.a += r

    def draw(self):
        self.screen.center_line(self.x, self.y, self.a, self.l)



def rotatePoint(a, px, py, cx, cy):  # angle, point to rotate x and y, pivot x and y


    #log("ra", a)
    rx = cos(a) * (px - cx) - sin(a) * (py - cy) + cx
    ry = sin(a) * (px - cx) + cos(a) * (py - cy) + cy
    return (rx, ry)



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
        scr.nodelay(1)                  # disable blocking
        screen = Screen(scr)            # renderer with curses default screen
        # board.line(0, 0, 5, 5)
        # board.y_screen()
        # board.num_screen()
        # board.random_screen()
        # board.simple_display()
        count = 0

        # gameBoard = GameBoard(3, 10, 20)

        temp = Line(5, 18, 35, 20, screen)

        d1 = 500
        d2 = 1000
        #grid = Grid(3, screen.w / 2, screen.h / 2, screen)


        #################################################################

        # points = [
        #     [-6, -6, -6],
        #     [-6,-0,-6],
        #     [6, -6, -6],
        #     [6, 6, -6],
        #     [6, 6, 6],
        #     [-6, 6, 6],
        #     [-6, -6, 6],
        #     [-6, 6, -6],
        #     [6, -6, 6],
        # ]
        points = [
            [-6, 6, 6],
            [6, 6, 6],
            [6, 6, 0],
            [6, 0, 6],
            [-6, 6, 6],
            [-6, 6, 0],
            [-6, 6, -6],
            [-6, 0, -6],
            [-6, -6, 0],
            [-6, -6, -6],
            [0, -6, 0],
            [6, -6, -6],
            [6, -6, 0],
            [6, -6, 6],
            [-6, 6, -6],
            [0, 6, 0],
            [-6, 0, 6],
            [0, 6, -6],
            [6,0,6],
            [0,0,-6],
            [6, 0, -6],
            [0, 6, 6],
            [6,6,-6],
            [0,-6,-6],
            [-6,-6,6],
            [0,-6,6],
            [0,0,6],
            [6,0,0],
            [-6,0,0]
        ]

            

        a = 0

        while True:
            c = scr.getch()
            screen.set(4, 3)
            # for x, i in enumerate(points):
            screen.clearScreen()


            for i in points:
                prj = project(rotateY(i, a),0,0)
                #screen.set(i[0]+screen.w/2, i[1]+screen.h/2)

                screen.set(((prj[0]*2.2)+screen.w/2), (prj[1]+screen.h/2))

            screen.curses_display()
            a += 0.03/2

        #################################################################

        # while True:
        #     grid = Grid(3, screen.w / 2, screen.h / 2, screen)
        #     logNoString("\ncycle\n\n")
        #     sc = count * 0.03 / 2
        #     mc = count * 0.03
        #     c = scr.getch()
        #     curses.flushinp()
        #     # scr.clear()
        #     screen.clearScreen()
        #
        #     # screen.center_line(screen.w / 2, screen.h / 2, sc, 25)
        #     # screen.center_v_line(screen.w / 2, screen.h / 2, 25)
        #     # screen.center_h_line(screen.w / 2, screen.h / 2, 25)
        #
        #     # gameBoard.x = gameBoard.x + 0.1
        #     # screen.draw_cross(gameBoard)
        #
        #
        #     #grid.scale(sin(sc))
        #     if count == d2:
        #         v = mc
        #     if count > d2:
        #         grid.scale(sin((sc-v))+1.3,sin((sc-v))+1.3)
        #     grid.rotate(sc*0.8)
        #     if count == d1:
        #         u = mc
        #     if count > d1:
        #        grid.translate(sin(mc-u)*20, 0)
        #
        #
        #
        #     grid.draw()
        #
        #     # temp.rotate(sc,18,25)
        #     # temp.draw()
        #
        #     screen.curses_display()
        #     time.sleep(0.001)
        #     count += 1

    wrapper(main)
