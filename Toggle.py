import pygame, pickle
pygame.mixer.init()

#load sounds
pygame.mixer.music.load(".\\Sound\\backgroundMusic.mp3")
flap = pygame.mixer.Sound(".\\Sound\\flap.mp3")
death = pygame.mixer.Sound(".\\Sound\\death.mp3")
coin = pygame.mixer.Sound(".\\Sound\\coin.mp3")
sfx = True

#load default graphics
backgroundSelect = 0
birdSelect = 0
pipeSelect = 0
backgroundList = [] 
floorList = []
birdList = []
pipeList = []
backgroundIconList = []
birdSIZE = (59, 42)
pipeSIZE = (100, 550)
backgroundSIZE = (600, 900)
floorSIZE = (600, 200)
lockIMG = pygame.transform.scale(pygame.image.load(".\\Sprites\\GameSprites\\locked.png"), (60,60))

#default save data
def resetData():    
    global saveData
    saveData = {
    "birdSave": [True, True, True, False, False, False, False, False, False],
    "pipeSave": [True, True, True, False, False, False, False, False, False],
    "backgroundSave": [True, True, False, False, False, False, False, False], 
    "highScore": 0.0,
    "coinCount": 0
    }
    print(saveData)

#required scores for unlocking skins            3 starter skins     6 unlockables
birdUnlocks = [10, 20, 30, 40, 50, 100]         #coin based
pipeUnlocks =  [5, 10, 15, 20, 25, 50]          #score based
#backgrounds will require you getting the "set" 
#ex: bird unlock 0 and pipe unlock 0 will get you back unlock 0

#get save data
def saveGame(sd):    
    with open("savaData.pickle", "wb") as f:
        pickle.dump(sd, f, pickle.HIGHEST_PROTOCOL)

#load save data
def loadGame():
    with open("savaData.pickle", "rb") as f:
        return pickle.load(f)

saveData = loadGame()

def startUp():  #starts music, gets all sprites loaded
    pygame.mixer.music.play(loops=-1)
    for x in [chr(i) for i in range(ord('a'), ord('z')+1)]:
        try:
            backIMG = pygame.image.load(f'.\\Sprites\\Background\\{x}.png')
            iconIMG = pygame.image.load(f'.\\Sprites\\BackgroundIcons\\{x}.png')
            backIMG = pygame.transform.scale(backIMG, backgroundSIZE)
            floorIMG = pygame.image.load(f'.\\Sprites\\Floor\\{x}.png')
            floorIMG = pygame.transform.scale(floorIMG, floorSIZE)
            backgroundList.append(backIMG)
            backgroundIconList.append(iconIMG)
            floorList.append(floorIMG)
        except:
            pass
        try:
            birdIMG = pygame.image.load(f'.\\Sprites\\Bird\\{x}.png')
            birdIMG = pygame.transform.scale(birdIMG, birdSIZE)
            birdList.append(birdIMG)
        except:
            pass
        try:
            pipeIMG = pygame.image.load(f'.\\Sprites\\Pipe\\{x}.png')
            pipeIMG = pygame.transform.scale(pipeIMG, pipeSIZE)
            pipeList.append(pipeIMG)
        except:
            pass
    saveData = loadGame()
    print(saveData)
    print("start up done")
    
def showBackground(display):
    display.blit(backgroundList[backgroundSelect], (0, 0))
    display.blit(floorList[backgroundSelect], (0, 700))

def musicToggle(music):
    if music==True:       #turn off
        pygame.mixer.music.pause()
        print("music off")
    else:
        if music==False:       #turn on
            pygame.mixer.music.unpause()
            print("music on")
    return not music

def sfxToggle(sfxT):
    global sfx
    if sfxT:
        sfx = False
        print("sfx off")
    else:
        if not sfxT:
            sfx = True
            print("sfx on")
    return sfx
                    
def playFlap():
    global sfx
    if sfx:
        flap.play()
        
def playDeath():
    global sfx
    if sfx:
        death.play()

def playCoin():
    global sfx
    if sfx:
        coin.play()    

#choose skins for bird/pipe/background
def birdRight():
    global birdSelect
    if birdSelect == 0:
        birdSelect = len(birdList)-1
    else:
        birdSelect-=1
    if saveData["birdSave"][birdSelect] == False:
        birdRight()

def birdLeft():
    global birdSelect
    if birdSelect == len(birdList)-1:
        birdSelect = 0
    else:
        birdSelect+=1
    if saveData["birdSave"][birdSelect] == False:
        birdLeft()

#if skin id is first/last in skin list, then add special function to show adjacent skins
def displayBird(display):  
    if birdSelect == 0: #first
        birdColor(birdSelect+1, display, (410, 250))        #right bird
        birdColor(birdSelect, display, (260, 245), 1.5)     #selected bird
        birdColor(len(birdList)-1, display, (140, 250))        #left bird
    elif birdSelect == len(birdList)-1: #last
        birdColor(0, display, (410, 250))                   #right bird
        birdColor(birdSelect, display, (260, 245), 1.5)     #selected bird
        birdColor(birdSelect-1, display, (140, 250))        #left bird
    else:
        birdColor(birdSelect+1, display, (410, 250))        #right bird
        birdColor(birdSelect, display, (260, 245), 1.5)     #selected bird
        birdColor(birdSelect-1, display, (140, 250))        #left bird

def birdColor(spriteSelect, display, coord, scale=1):
    img = birdList[spriteSelect]
    img = pygame.transform.scale_by(img, scale)
    if saveData["birdSave"][spriteSelect] == False:
        display.blit(img, coord)
        display.blit(lockIMG, (coord[0], coord[1]-5))
    else:
        display.blit(img, coord)

def backgroundRight():
    global backgroundSelect
    if backgroundSelect == 0:
        backgroundSelect = len(backgroundList)-1
    else:
        backgroundSelect-=1
    if saveData["backgroundSave"][backgroundSelect] == False:
        backgroundRight()

def backgroundLeft():
    global backgroundSelect
    if backgroundSelect == len(backgroundList)-1:
        backgroundSelect = 0
    else:
        backgroundSelect+=1
    if saveData["backgroundSave"][backgroundSelect] == False:
        backgroundLeft()

def showBackgrounds(left, center, right, display):
    display.blit(right, (415, 595))        #right pipe
    display.blit(center, (260, 585))       #selected pipe
    display.blit(left, (140, 595))         #left pipe

def displayBackground(display):
    selectedBackground = pygame.transform.scale_by(backgroundIconList[backgroundSelect], .6)
    if backgroundSelect == 0: #first
        backgroundColor(backgroundSelect+1, display, (415, 595))        #right
        backgroundColor(backgroundSelect, display, (260, 585), .6)    #center
        backgroundColor(len(backgroundIconList)-1, display, (140, 595))        #left
    elif backgroundSelect == len(backgroundIconList)-1: #last
        backgroundColor(0, display, (415, 595))                         #right
        backgroundColor(backgroundSelect, display, (260, 585), .6)      #center
        backgroundColor(backgroundSelect-1, display, (140, 595))        #left
    else:
        backgroundColor(backgroundSelect+1, display, (415, 595))        #right
        backgroundColor(backgroundSelect, display, (260, 585), .6)      #center
        backgroundColor(backgroundSelect-1, display, (140, 595))        #left
        
def backgroundColor(spriteSelect, display, coord, scale=.4):
    img = backgroundIconList[spriteSelect]
    img = pygame.transform.scale_by(img, scale)
    if saveData["backgroundSave"][spriteSelect] == False:
        display.blit(img, coord)
        display.blit(lockIMG, (coord[0], coord[1]-5))
    else:
        display.blit(img, coord)
        
def pipeRight():
    global pipeSelect
    if pipeSelect == 0:
        pipeSelect = len(pipeList)-1
    else:
        pipeSelect-=1
    if saveData["pipeSave"][pipeSelect] == False:
        pipeRight()

def pipeLeft():
    global pipeSelect
    if pipeSelect == len(pipeList)-1:
        pipeSelect = 0
    else:
        pipeSelect+=1
    if saveData["pipeSave"][pipeSelect] == False:
        pipeLeft()

def showPipes(right, center, left, display):
    #to crop = disp.blit(img, (xpos, ypos), (xcrop, ycrop, cropwidth, cropheight))
    display.blit(right, (415, 425), (0, 0, 100, 75))            #right pipe
    display.blit(center, (265, 415), (0, 0, 100, 85))                      #selected pipe
    display.blit(left, (140, 425), (0, 0, 100, 75))         #left pipe
        
def displayPipe(display):
    selectedPipe = pygame.transform.scale_by(pipeList[pipeSelect], .75)    
    if pipeSelect == 0: #first
        pipeColor(pipeSelect+1, display, (415, 425), (0, 0, 100, 75))           #right
        pipeColor(pipeSelect, display, (265, 415), (0, 0, 100, 85), .75)        #center
        pipeColor(len(pipeList)-1, display, (140, 425), (0, 0, 100, 75))        #left
    elif pipeSelect == len(pipeList)-1: #last
        pipeColor(0, display, (415, 425), (0, 0, 100, 75))                      #right
        pipeColor(pipeSelect, display, (265, 415), (0, 0, 100, 85), .75)        #center
        pipeColor(pipeSelect-1, display, (140, 425), (0, 0, 100, 75))           #left
    else:
        pipeColor(pipeSelect+1, display, (415, 425), (0, 0, 100, 75))           #right
        pipeColor(pipeSelect, display, (265, 415), (0, 0, 100, 85), .75)        #center
        pipeColor(pipeSelect-1, display, (140, 425), (0, 0, 100, 75))           #left

def pipeColor(spriteSelect, display, coord, crop, scale=.5):
    img = pipeList[spriteSelect]
    img = pygame.transform.scale_by(img, scale)
    if saveData["pipeSave"][spriteSelect] == False:
        display.blit(img, coord, crop)
        display.blit(lockIMG, (coord[0], coord[1]-5))
    else:
        display.blit(img, coord, crop)
        
def displayArrows(display):
    arrow = pygame.image.load(".\\Sprites\\GameSprites\\arrowWhite.png")
    arrowR = pygame.transform.flip(arrow, 1, 0)
    display.blit(arrow, (205, 250))     #bird left
    display.blit(arrowR, (350, 250))     #bird right
    display.blit(arrow, (205, 425))     #pipe left
    display.blit(arrowR, (350, 425))     #pipe right
    display.blit(arrow, (205, 600))     #back left
    display.blit(arrowR, (350, 600))     #back rights
    
def quitGame():
    saveGame(saveData)
    print(saveData)
    exit()
    
def gameUpdate():
    pipeHold = 0        #pipe update
    for x in pipeUnlocks:
        if saveData["highScore"] >= x:
            pipeHold += 1
    for x in range(0, pipeHold):
        saveData["pipeSave"][x+3] = True 
        
    birdHold = 0        #bird update
    for x in birdUnlocks:
        if saveData["coinCount"] >= x:
            birdHold += 1
    for x in range(0, birdHold):
        saveData["birdSave"][x+3] = True 
        
    backgroundHold = min(birdHold, pipeHold)
    for x in range(0, backgroundHold):
        saveData["backgroundSave"][x+2] = True 
    print(saveData)


        
