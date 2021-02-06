import curses
import datetime
import vlc
import time
import pickle

import util

filename = input("Which file do you want to create a track for?")

p = vlc.MediaPlayer(filename)

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1)

notes = []

try:
    trackLength = 0
    lastDraw = time.time()
    playing = False
    currentTime = 0
    while 1:
        #currentTime = p.get_time()
        c = stdscr.getch()
        if c == ord('q'):
            break
        if c == ord('p'):
            p.pause()
        if c == ord('s'):
            p.play()
            trackLength = p.get_length()
        if c == ord('h'):
            currentTime = p.get_time()
            p.set_time(currentTime-1000)
        if c == ord('l'):
            currentTime = p.get_time()
            p.set_time(currentTime+1000)
        if c == ord('j'):
            currentTime = p.get_time() 
            p.set_time(currentTime-100)
        if c == ord('k'):
            currentTime = p.get_time()
            p.set_time(currentTime+100)
        if c == ord('1'):
            currentTime = p.get_time()
            notes.append((1, currentTime, currentTime))
        if c == ord('2'):
            currentTime = p.get_time()
            notes.append((2, currentTime, currentTime))
        if c == ord('3'):
            currentTime = p.get_time()
            notes.append((3, currentTime, currentTime))
        if c == ord('4'):
            currentTime = p.get_time()
            notes.append((4, currentTime, currentTime))
        if c == ord('5'):
            currentTime = p.get_time()
            notes.append((5, currentTime, currentTime))

        if time.time() - lastDraw > 0.1:
            currentTime = p.get_time()
            util.redraw(stdscr, currentTime/1000, notes)
            lastDraw = time.time()

         
        stdscr.addstr(40,0, str(currentTime/1000)+":"+str(trackLength/1000))
finally:
    pickle.dump(notes, open('test2', 'wb'))
    curses.endwin()
