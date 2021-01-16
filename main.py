import pyfiglet
import os
import time
import keyboard

def gameLoop(song):
    #for each line in the song
    notesHit = 0
    notesMishit = 0
    notesMissed = 0
    for i in range (0, len(song)):

        for j in range(0, 9, 1):
            if i - j > 0:
                
                if j == 8:
                    s = list(song[i-j])
                    s[1] = '['
                    s[3] = ']'
                    s[5] = '['
                    s[7] = ']'
                    s[9] = '['
                    s[11] = ']'
                    s[13] = '['
                    s[15] = ']'
                    s[17] = '['
                    s[19] = ']'
                    print("".join(s))
                else:
                    print(song[i-j])
            else:
                if j == 8:
                    print("|[ ]|[ ]|[ ]|[ ]|[ ]|")
                else:
                    print("|   |   |   |   |   |")
        pressedKeys = [0,0,0,0,0]
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("notesHit: " + str(notesHit))
        print("notesMissed: " + str(notesMissed))
        print("notesMishit: " + str(notesMishit))
        
        line = list(song[i-8])
        print(line)
        time.sleep(0.2)
        try:
            if keyboard.is_pressed("1"):
                pressedKeys[0] = 1
                if line[2] == 'X':
                    notesHit += 1
                else:
                    notesMishit +=1
                
            if keyboard.is_pressed('2'):
                pressedKeys[1] = 1
                if line[6] == 'X':
                    notesHit += 1
                else:
                    notesMishit +=1
                
            if keyboard.is_pressed('3'):
                pressedKeys[2] = 1
                if line[10] == 'X':
                    notesHit += 1
                else:
                    notesMishit +=1
            
            if keyboard.is_pressed('4'):
                pressedKeys[3] = 1
                if line[14] == 'X':
                    notesHit += 1
                else:
                    notesMishit +=1

            if keyboard.is_pressed('5'):
                pressedKeys[4] = 1
                if line[18] == 'X':
                    notesHit += 1
                else:
                    notesMishit +=1
                
        except:
            pass
        time.sleep(0.2)
        if pressedKeys[0] == 0 and line[2] == 'X':
            notesMissed += 1
        if pressedKeys[1] == 0 and line[6] == 'X':
            notesMissed += 1
        if pressedKeys[2] == 0 and line[10] == 'X':
            notesMissed += 1
        if pressedKeys[3] == 0 and line[14] == 'X':
            notesMissed += 1
        if pressedKeys[4] == 0 and line[18] == 'X':
            notesMissed += 1

        
        os.system('cls' if os.name == 'nt' else 'clear')

    print("FINAL SCORE")
    print("notesHit: " + str(notesHit))
    print("notesMissed: " + str(notesMissed))
    print("notesMishit: " + str(notesMishit))


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_banner = pyfiglet.figlet_format("GUITARPY")
    print(ascii_banner)
    songs = []
    #get all songs available
    for file in os.listdir("songs"):
        if file.endswith(".txt"):
            songs.append(file)
    
    print("WHICH ROCKIN' SONG DO YOU WANNA PLAY?")
    for i in range(0,len(songs)):
        print (str(i) + " - " + songs[i])

    songChoice = int(input(">"))

    songFile = "songs/"+songs[songChoice]

    content = []

    with open(songFile) as f:
        content = f.readlines()
        content = [x.strip() for x in content] 

    gameLoop(content)

        

    
    