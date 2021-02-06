import curses
import datetime
import vlc
import time
import functools
import math


def redraw(stdscr, t, notes):
    notesToDraw = [n for n in notes if n[1]/1000 <= t + 3 and n[1]/1000 >= t-1]
    notesOnAdjustedLines = [(n[0], math.ceil((n[1]-t*1000) / 90), n[2]) for n in notesToDraw]
    stdscr.addstr(31,0,str(notesToDraw))
    stdscr.addstr(32,0,str(t))
    stdscr.addstr(33,0,str(notesOnAdjustedLines))
    for i in range (0, 30, 1):
        stdscr.addstr(35,0,str(i))
        
        notesToDraw = [n[0] for n in notesOnAdjustedLines if n[1] == i]
        
        if i != 0:
            lineString = "|"
            for j in range (1,6):
                if j in notesToDraw:
                    lineString += "| X |"
                else:
                    lineString += "|   |"
            lineString += "|"
        else:
            lineString = "["
            for j in range (1,6):
                if j in notesToDraw:
                    lineString += "[ X ]"
                else:
                    lineString += "[   ]"
            lineString += "]"
        
        stdscr.addstr(30-i, 0, lineString)



p = vlc.MediaPlayer("test.mp3")
p.play()

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1) # set getch() non-blocking

# note, start, finish
notes = [(1, 5000, 5000),(2,3000,3000), (3,4000,4000)]

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
            
        stdscr.addstr(38, 0, "points: " + str(score)) 
        stdscr.addstr(39,0,str(notesPressed))
        if c == ord('x'):
            break
        if now - lastDraw > rrate:
            stdscr.addstr(0,0,str(now - lastDraw))
            
            lastDraw = now
            redraw(stdscr, now-startTime, notes)
            

finally:
    curses.endwin()

