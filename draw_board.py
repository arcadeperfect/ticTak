import locale
import curses
from curses import wrapper

locale.setlocale(locale.LC_ALL, '')


def draw_h_line(scr,y,x,l, ch = u'\u2501'):
    for i in range(l):
        scr.addstr(y, x+i, ch)


def draw_v_line(scr,y,x,l, ch = u'\u2502'):
    for i in range(l):
        scr.addstr(y+i, x, ch)

def main(stdscr):
    scr = curses.initscr()
    scr.clear()
    z = u'\u2501'.encode('utf-8')
    h_line_char = u'\u2501'
    v_line_char = u'\u2503'
    v = u'\u007c'

    # scr.addstr(0, 0, v)
    # scr.addstr(1, 0, v)
    # scr.addstr(2, 0, v)
    # draw_h_line(scr,3,4,50)
    # draw_v_line(scr,3,4,10)
    # scr.hline("a",20)
    scr.wvline(0,10,v)
    scr.getch()

wrapper(main)