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

