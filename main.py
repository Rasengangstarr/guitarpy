import curses
import datetime
import vlc
import time
import functools
import math
import pickle
import util
import pyfiglet

p = vlc.MediaPlayer("test2.mp3")
p.play()

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1) # set getch() non-blocking

# note, start, finish
notes = pickle.load(open('test2', 'rb'))

rrate = 0.1
rprecision = 100
stdscr.addstr(0,0,"Press \"p\" to show count, \"q\" to exit...")
line = 1
try:
    count = 1
    startTime = time.time()
    lastDraw = time.time()
    score = 0
    notesPressed = [0,0,0,0,0]

    while 1:
        now = time.time()
        currentNotes = [n[0] for n in notes if n[1] >= round((now - startTime) * 1000) - rprecision and n[1] <= round((now - startTime) * 1000) + rprecision ]
        stdscr.addstr(36,0,str(round((now-startTime)*1000)))
        if len(currentNotes) > 0:
            stdscr.addstr(34,0,str(currentNotes))
        
        c = stdscr.getch()
        if c != -1:
            stdscr.addstr(40,0,str(c))
        if c == ord('1'):
            if 1 in currentNotes:
                score += 1
        if c == ord('2'):
            if 2 in currentNotes:
                score += 1
        if c == ord('3'):
            if 3 in currentNotes:
                score += 1
        if c == ord('4'):
            if 4 in currentNotes:
                score += 1
        if c == ord('5'):
            if 5 in currentNotes:
                score += 1
            
        stdscr.addstr(40, 0, pyfiglet.figlet_format("points: " + str(score))) 
        stdscr.addstr(39,0,str(notesPressed))
        if c == ord('x'):
            break
        if now - lastDraw > rrate:
            stdscr.addstr(0,0,str(now - lastDraw))
            
            lastDraw = now
            util.redraw(stdscr, now-startTime, notes)
            

finally:
    curses.endwin()

