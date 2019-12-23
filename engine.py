import curses
from curses import wrapper

#
# class Board:
#     def __init__(self):

board_width = 3
board_height = 3

w = (board_width)*2+1
h = (board_height)*2+1

v_bar = "│"
h_bar = "─"
cross = "┼"
p1 = "x"
p2 = "o"

#screen = [["{},{}".format(y,x) for x in range(w)] for y in range(h)]
#
# screen = [[None for x in range(w)] for y in range(h)]

screen = [[None for x in range(w)] for y in range(h)]



def hLine(y,x,l):
    for i in range(l):

        if screen[y][x+i] == v_bar:
            screen[y][x + i] = cross
        else:
            screen[y][x+i] = h_bar

def vLine(y,x,l):
    for i in range(l):
        if screen[y + i][x] == h_bar:
            screen[y + i][x]  = cross
        else:
            screen[y+i][x] = v_bar

def p1_piece(y,x):
    if screen[y][x] == " ":
        screen[y][x] = p1
    else:
        raise Exception('space not empty')

def p2_piece(y,x):
    if screen[y][x] == " ":
        screen[y][x] = p2
    else:
        raise Exception('space not empty')


def simpleDraw():

    for y in range(h):
        for x in range(w):
            z = screen[y][x]
            if z is None:
                char = "n"
            else:
                char = z
            print(char, end = "")

        print("")


for i in range(w):
    if i%2==0:
        vLine(0,i,h)

for i in range(h):
    if i%2==0:
        hLine(i,0,w)

#
# vLine(0,6,h)
#
#
# hLine(4,0,w)
#
#
# p2_piece(1,4)

print(w,h)

simpleDraw()




