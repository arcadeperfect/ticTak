import locale
import curses
from curses import wrapper

locale.setlocale(locale.LC_ALL, '')

read = ''

def draw_h_line(scr, y, x, l):
    for i in range(l):
        if scr.inch(y, x+i,) == curses.ACS_VLINE:
            scr.addch(y, x + i, "o")
        else:
            scr.addch(y, x + i, curses.ACS_HLINE)


def draw_v_line(scr, y, x, l):
    for i in range(l):
        scr.addch(y + i, x, curses.ACS_VLINE)

vline = ''

def main(stdscr):
    scr = curses.initscr()
    scr.clear()

    draw_h_line(scr, 3, 0, 5)
    draw_v_line(scr, 0, 3, 5)
    print(scr.inch(0, 3))

    scr.getch()
    read = scr.inch(3,0)

    scr.addch(2,2,scr.inch(3,0))
    vline = curses.ACS_VLINE
    return vline

wrapper(main)

print main(stdscr)
print(read)
print(vline)