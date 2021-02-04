import curses
import datetime
import vlc
import time
import functools
import math


def redraw(stdscr, t, notes):
    notesToDraw = [n for n in notes if n[1]/1000 < t + 3 and n[1]/1000 > t]
    notesOnAdjustedLines = [(n[0], math.ceil((n[1]-t*1000) / 30), n[2]) for n in notesToDraw]
    stdscr.addstr(31,0,str(notesToDraw))
    stdscr.addstr(32,0,str(t))
    stdscr.addstr(33,0,str(notesOnAdjustedLines))
    for i in range (0, 30):
        noteToDraw = [n for n in notesOnAdjustedLines if n[1] == i]
        if len(noteToDraw) > 0:
            stdscr.addstr(i,0,str(noteToDraw[0][1] ))
        else:
            stdscr.addstr(i,0,"nout")




p = vlc.MediaPlayer("TEST_SONG.mp3")
#p.play()

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1) # set getch() non-blocking

# note, start, finish
notes = [(1, 5000, 5000)]

stdscr.addstr(0,0,"Press \"p\" to show count, \"q\" to exit...")
line = 1
try:
    count = 1
    startTime = time.time()
    lastDraw = time.time()
    while 1:
        now = time.time()
        c = stdscr.getch()
        #if c == ord('1'):
        #    stdscr.addstr(line,0,str(count))
        #    line += 1
        if c == ord('x'):
            break
        if now - lastDraw > 0.01:
            stdscr.addstr(0,0,str(now - lastDraw))
            
            lastDraw = now
            redraw(stdscr, now-startTime, notes)
            

finally:
    curses.endwin()

