import curses
from curses import wrapper


def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.addstr("test")
    stdscr.addstr(3, 3, "x")
    stdscr.addstr(6, 6, "x")
    stdscr.clear()
    n = 0
    while True:

        c = stdscr.getch()
        stdscr.clear()
        stdscr.addstr(str(n))
        stdscr.move(2, 0)
        if c == curses.KEY_UP:
            stdscr.addstr("up")
        elif c == curses.KEY_DOWN:
            stdscr.addstr("down")
        elif c == curses.KEY_LEFT:
            stdscr.addstr("left")
        elif c == curses.KEY_RIGHT:
            stdscr.addstr("right")
        elif c == curses.KEY_ENTER or c == 10 or c == 13:
            stdscr.addstr("enter")

        n +=1

wrapper(main)