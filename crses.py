import curses
from curses import wrapper
from engine import Board


def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.addstr("test")
    stdscr.addstr(3, 3, "x")
    stdscr.addstr(6, 6, "x")
    stdscr.clear()
    n = 0
    board = Board()
    while True:

        stdscr.clear()
        board.cursesDisplay(stdscr)
        p = stdscr.getyx()
        c = stdscr.getch()
        stdscr.move(2, 0)
        print(p)
        stdscr.move(1,3)
        # if c == curses.KEY_UP:
        #     stdscr.move(p[0] + 1, p[1])
        # elif c == curses.KEY_DOWN:
        #     stdscr.move(p[0] - 1, p[1])
        # elif c == curses.KEY_LEFT:
        #     stdscr.move(p[0], p[1] - 1)
        # elif c == curses.KEY_RIGHT:
        #     stdscr.move(p[0], p[1] + 1)
        # elif c == curses.KEY_ENTER or c == 10 or c == 13:
        #     stdscr.move(p[0] + 1, p[1])

        n += 1


wrapper(main)

board = Board()

board = Board()

screen = board.screen

for y in range(board.h):
    for x in range(board.w):
        cell = screen[y][x]
        if cell is not None:
            print(cell)
