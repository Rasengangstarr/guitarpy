import curses
import datetime
import vlc
import time

import util

filename = input("Which file do you want to create a track for?")

p = vlc.MediaPlayer(filename)

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1)

notes = [(1,5000,5000), (2, 3000,3000),(3,2000,2000)]

try:
    trackLength = 0
    lastDraw = time.time()
    playing = False
    while 1:
        currentTime = p.get_time()
        c = stdscr.getch()
        if c == ord('q'):
            break
        if c == ord('p'):
            p.pause()
        if c == ord('s'):
            p.play()
            trackLength = p.get_length()
        if c == ord('h'):
            p.set_time(currentTime-1000)
        if c == ord('l'):
            p.set_time(currentTime+1000)
        if c == ord('j'):
            p.set_time(currentTime-100)
        if c == ord('k'):
            p.set_time(currentTime+100)

        if time.time() - lastDraw > 0.1:
            util.redraw(stdscr, currentTime/1000, notes)
            lastDraw = time.time()

    
        stdscr.addstr(40,0, str(currentTime/1000)+":"+str(trackLength/1000))
finally:
    curses.endwin()
