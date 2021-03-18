import curses
import time
import random
import os

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

def main2(screen):
    # Clear screen
    screen.clear()
    # screen.keypad(True)

    # curses.echo()
    while True:
        key = screen.getkey()

        screen.addstr(key)
        if key == "\n":
            screen.addstr(chr(13) + chr(10) + "heiiheihey_"+key)
            # screen.addstr("\n")

        # screen.refresh()
    # print(curses.can_change_color(), "##########################################################################")
    # screen.addstr(0, 0, chr(13)+chr(10)+"key:"+key, curses.color_pair(1))
    # curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # screen.addstr("Pretty text", curses.color_pair(1))

    print(chr(13)+chr(10)+"key:", key)
    ch = screen.getch()
    print("ch:", chr(ch))
    time.sleep(1)

def moveRel(screen, y, x):
    oldY, oldX = screen.getyx()
    newY = oldY + y
    newX = oldX + x
    if newY >= 0 and newY < curses.LINES and newX >= 0 and newX < curses.COLS:
        screen.move(newY, newX)


def myVim(screen):
    # Config:
    config = {
        "move": {
            "up": [curses.KEY_UP, ord("k")],
            "right": [curses.KEY_RIGHT, ord("l")],
            "down": [curses.KEY_DOWN, ord("j")],
            "left": [curses.KEY_LEFT, ord("h")],
            "insert": [ord("i")],
        },
        "insert": {
            "escape": [0x1b],
            "backspace": [curses.KEY_BACKSPACE],
        }
    }

    # Allowed modes
    # - move
    # - insert
    mode = "move"

    screen.clear()

    while True:
        tempyx = screen.getyx()
        screen.move(curses.LINES - 1, 0)
        screen.clrtoeol()
        screen.addstr("Mode: " + mode)
        screen.move(*tempyx)
        screen.refresh()
        key = screen.getch()
        if mode == "move":
            if key in config["move"]["up"]:
                moveRel(screen, -1, 0)
            elif key in config["move"]["right"]:
                moveRel(screen, 0, 1)
            elif key in config["move"]["down"]:
                moveRel(screen, 1, 0)
            elif key in config["move"]["left"]:
                moveRel(screen, 0, -1)
            elif key in config["move"]["insert"]:
                mode = "insert"
        elif mode == "insert":
            if key in config["insert"]["escape"]:
                mode = "move"
            elif key in config["insert"]["backspace"]:
                moveRel(screen, 0, -1)
                screen.delch()
            else:
                screen.addstr(chr(key))

def mouseTest(screen):
    screen.clear()
    availmask, oldmask = curses.mousemask(curses.ALL_MOUSE_EVENTS)
    screen.addstr(f"av: 0b{availmask:b}, old: 0b{oldmask:b}, all: 0b{curses.ALL_MOUSE_EVENTS:b}\n")
    screen.addstr(f"lines: {curses.LINES}, cols: {curses.COLS}")

    while True:
        ch = screen.getch()
        screen.addstr("X")
        if ch == curses.KEY_MOUSE:
            idd, x, y, z, bstate = curses.getmouse()
            screen.move(y, x)
            screen.addstr(f"y: {y}, x: {x}")
        else:
            screen.addstr("ting:" + chr(ch))

os.environ.setdefault("ESCDELAY", "25")
curses.wrapper(mouseTest)
