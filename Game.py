import pygame, Toggle, random

#setup           rect = (pos), (size)        (x, y)

def gameRun(display, fps):
    #setup game
    pipeS = Toggle.pipeList[Toggle.pipeSelect]
    birdS = Toggle.birdList[Toggle.birdSelect]
    backgroundS = Toggle.backgroundList[Toggle.backgroundSelect]
    floorS = Toggle.floorList[Toggle.backgroundSelect]
    
    birdY = 350     #starting height
    birdVel = 0
    yMaxVel = 25
    accel = 2
    score = 0
    
    prevScore = Toggle.saveData["highScore"]
    prevCoin = Toggle.saveData["coinCount"]
    coin = False
    
    
    pipeList = []       #list of pipe images
    pipeTimer = 150     #countdown for new pipe
    pipeList.append(newPipe(pipeS, score, coin))   #starting pipe
    
    #gaming loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):       #handles QUIT anytime
                print("exiting")
                Toggle.quitGame()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                print("return to main")
                return
            elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP)) or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1): 
                Toggle.playFlap()
                birdVel = -18
            else:
                pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
        
        #creates new pipe according to difficulty
        if pipeTimer <= 0:   
            if random.randint(0, 5) == 3:   #coin
                coin = True
            newestPipe = newPipe(pipeS, score, coin)
            coin = False
            pipeList.append(newestPipe)
            if score >=50:
                pipeTimer = 100
            else:
                pipeTimer = 150-score
        else:
            pipeTimer-=2        #decrease pipe countdown
        
        pipeList = updatePipes(pipeList)
        
        #falling bird
        if birdVel <= yMaxVel:
            birdVel += accel
        else:
            birdVel = yMaxVel
        birdY += birdVel
        
        #score increase
        if 97 < pipeList[0][4] < 103:
            score+=5
            print(score)
        
        #coin detection
        if 50 < pipeList[0][4] < 125:
            cy = pipeList[0][7]
            if pipeList[0][5] and (cy-41 < birdY  and birdY < cy+50):
                Toggle.saveData["coinCount"] += 1
                pipeList[0][5] = False
                Toggle.playCoin()
                print("coin collected")
            
        if isGameOver(birdY, pipeList[0], score):
            if prevScore != Toggle.saveData["highScore"] or prevCoin != Toggle.saveData["coinCount"]:
                Toggle.gameUpdate()
            return
        
        display.blit(backgroundS, (0,0))
        for pipe in pipeList:       #display pipes
            display.blit(pipe[0], (pipe[4], pipe[1]))
            display.blit(pipe[2], (pipe[4], pipe[3]))
            if pipe[5]:
                display.blit(pipe[6], (pipe[4]+25, pipe[7]))
        display.blit(birdS, (100, birdY))
        display.blit(floorS, (0,700))
        pygame.display.update()
        fps.tick(30)


def updatePipes(pipes):
    for pipe in pipes:      #update pipes
        pipe[4]-=6
        if pipe[4] <= -101:
            print("first pipe updated")
            pipes.pop(0)
    return pipes


def isGameOver(yCoord, pipes, score):
    score = score/5
    if 1 < pipes[4] < 150 :
            #top pipe                   bottom pipe
        if (yCoord <= pipes[1]+550) or (yCoord+42 >= pipes[3]):
            print("game over")
            if Toggle.saveData["highScore"] <= score:
                Toggle.saveData["highScore"] = score
            print(Toggle.saveData)
            Toggle.playDeath()
            return True
        #top of screen   floor
    if (yCoord <=0) or (yCoord >= 660):
        print("game over")
        if Toggle.saveData["highScore"] < score:
            Toggle.saveData["highScore"] = score
        print(Toggle.saveData)
        Toggle.playDeath()
        return True
    return False

def newPipe(pipe, score, newCoin):
    #pipe shenanigans
    pipeTop = pygame.transform.flip(pipe, 0, 1)
    pipeBottom = pipe
    if score > 45:
        pipeOffset = 150
    elif score <5:
        pipeOffset = 400
    else:
        scoreMax = int(score/5)*25
        scoreMin = (int(score/5)-1)*25
        pipeOffset = 400 - random.randint(scoreMin, scoreMax)
    pipeY = random.randint(-500, -200)
    if ((pipeY + pipeOffset + 550) > 650):
        pipeYB = 650
    else:
        pipeYB = pipeY + pipeOffset + 550
    print("pipe created")

    coinTF = False
    if newCoin:
        coinTF = True
        coinY = int((pipeYB + pipeY + 550)/2-25)
        coinIMG = pygame.image.load(".\\Sprites\\GameSprites\\coin.png")
    else:
        coinY = 0
        coinIMG = 0
    
    return [pipeTop, pipeY, pipeBottom, pipeYB, 600, coinTF, coinIMG, coinY]