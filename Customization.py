import pygame, Toggle, Game
pygame.font.init()

#setup           rect = (pos), (size)        (x, y)
mode = 2
playR = pygame.Rect((100, 788), (75, 75))
backR = pygame.Rect((425, 788), (75, 75))
birdR = pygame.Rect((100, 225), (400, 100))
pipeR = pygame.Rect((100, 400), (400, 100))
backgroundR = pygame.Rect((100, 575), (400, 100))

birdRight = pygame.Rect((205, 250), (50, 50))
birdLeft = pygame.Rect((350, 250), (50, 50))
pipeRight = pygame.Rect((205, 425), (50, 50))
pipeLeft = pygame.Rect((350, 425), (50, 50))
backgroundRight = pygame.Rect((205, 600), (50, 50))
backgroundLeft = pygame.Rect((350, 600), (50, 50))

playSprite = pygame.image.load(".\\Sprites\\GameSprites\\playSmall.png")
backSprite = pygame.image.load(".\\Sprites\\GameSprites\\back.png")

def customizationRun(display, fps, header):
    header = pygame.transform.scale_by(header, 2)
    while(True):
        Toggle.showBackground(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):       #handles QUIT anytime
                print("exiting")
                Toggle.quitGame()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                print("return to main")
                return
            else:
                pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
        
        mouseCoord = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
        Toggle.displayArrows(display)         #show arrows
        #                           color       x, y, width, height
        pygame.draw.rect(display, [0, 0, 0], [100, 225, 400, 100], 1)
        pygame.draw.rect(display, [0, 0, 0], [100, 400, 400, 100], 1)
        pygame.draw.rect(display, [0, 0, 0], [100, 575, 400, 100], 1)
        
        #bird customization
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     #right, birdSelect + 1
            if birdRight.collidepoint(mouseCoord):        #click
                Toggle.birdRight()
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                print("bird change left")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     #left, birdSelect - 1
            if birdLeft.collidepoint(mouseCoord):        #click
                Toggle.birdLeft()
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                print("bird change right")


        #back customization
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     #right, backgroundSelect + 1
            if backgroundRight.collidepoint(mouseCoord):        #click
                Toggle.backgroundRight()
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                print("background change left")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     #left, backgroundSelect - 1
            if backgroundLeft.collidepoint(mouseCoord):        #click
                Toggle.backgroundLeft()
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                print("background change right")
                

        #pipe customization
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     #right, pipeSelect + 1
            if pipeRight.collidepoint(mouseCoord):        #click
                Toggle.pipeRight()
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                print("pipe change left")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:     #left, pipeSelect - 1
            if pipeLeft.collidepoint(mouseCoord):        #click
                Toggle.pipeLeft()
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
                print("pipe change right")
        
        #play
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if playR.collidepoint(mouseCoord):      #start game
                print("game start")
                Game.gameRun(display, fps)
                return
        
        #back
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if backR.collidepoint(mouseCoord):      #return to main menu
                print("return to main")
                return
        
        #display sprites and update display
        display.blit(header, (0,0))
        Toggle.displayBird(display)
        Toggle.displayBackground(display)
        Toggle.displayPipe(display)
        display.blit(playSprite, (100, 788))
        display.blit(backSprite, (425, 788))
        pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
        pygame.display.update()
        fps.tick(30)
