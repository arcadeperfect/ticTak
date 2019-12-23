import curses
from curses import wrapper

def main(stdscr):


    gameWindow = curses.initscr()

    boardWinHeight = 10
    boardWinWidth = 10

    for y in range(0,boardWinHeight):
        for x in range(0,boardWinWidth):
            if y == 0:
                if x % 2 == 0:
                    gameWindow.addch(y,x,curses.ACS_TTEE,curses.A_DIM)
                else:
                    gameWindow.addch(y,x,curses.ACS_HLINE,curses.A_DIM)
            elif x == 0:
                if y % 2 == 0:
                    gameWindow.addch(y,x,curses.ACS_LTEE,curses.A_DIM)
                else:
                    gameWindow.addch(y,x,curses.ACS_VLINE,curses.A_DIM)
            elif y == boardWinHeight-1:
                if x < boardWinWidth-1:
                    if x % 2 == 0:
                        gameWindow.addch(y,x,curses.ACS_BTEE,curses.A_DIM)
                    else:
                        #gameWindow.c
                        pass
            elif x == boardWinWidth-1:
                if y % 2 == 0:
                    gameWindow.addch(y,x,curses.ACS_RTEE,curses.A_DIM)
                else:
                    gameWindow.addch(y,x,curses.ACS_VLINE,curses.A_DIM)
            else:
                if y % 2 == 0 and x % 2 == 1:
                    gameWindow.addch(y,x,curses.ACS_HLINE,curses.A_DIM)
                elif y % 2 == 1 and x % 2 == 0:
                    gameWindow.addch(y,x,curses.ACS_VLINE,curses.A_DIM)
                elif y % 2 == 0 and x % 2 == 0:
                    gameWindow.addch(y,x,curses.ACS_PLUS,curses.A_DIM)
    gameWindow.addch(0,0,curses.ACS_ULCORNER,curses.A_DIM)
    gameWindow.addch(0,boardWinWidth-1,curses.ACS_URCORNER,curses.A_DIM)
    gameWindow.addch(boardWinHeight-1,0,curses.ACS_LLCORNER,curses.A_DIM)

    gameWindow.getch()


wrapper(main)