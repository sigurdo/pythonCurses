import curses
import time
import random

# Automatically did by curses.wrapper():
# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)

# Do stuff

# # Terminate curses:
# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()
# curses.endwin()

# curses.initscr()

def main(screen):
    # Clear screen
    screen.clear()

    begin_x = 20
    begin_y = 7
    height = 5
    width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    win.addstr(2, 0, "hmmmmmmhmhm")

    # while True:
    #     screen.addstr(0, 0, "Lines:"+str(curses.LINES))
    #     # print("heyho")
    #     screen.refresh()
    #     time.sleep(1)

    pad = curses.newpad(1000, 1000)
    for y in range(999):
        for x in range(999):
            pad.addch(y, x, ord("a") + (x * x + y * y) % 26)

    screen.refresh()
    win.refresh()
    pad.refresh(0, 0, 5, 5, curses.LINES - 1, curses.COLS - 1)
    key = screen.getkey()
    # print(curses.can_change_color(), "##########################################################################")
    screen.addstr(0, 0, chr(13)+chr(10)+"key:"+key, curses.color_pair(1))
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    screen.addstr("Pretty text", curses.color_pair(1))
    screen.refresh()

    print(chr(13)+chr(10)+"key:", key)
    ch = screen.getch()
    print("ch:", chr(ch))
    time.sleep(1)

curses.wrapper(main)
