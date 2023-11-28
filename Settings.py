import pygame, Toggle, Game

#setup          rect = (pos), (size)        (x, y)
mode = 3
musicR = pygame.Rect((125, 250), (125, 125))
sfxR = pygame.Rect((375, 250), (125, 125))
playR = pygame.Rect((100, 788), (75, 75))
backR = pygame.Rect((425, 788), (75, 75))
musicT = sfxT = True

musicOn = pygame.image.load(".\\Sprites\\GameSprites\\musicOn.png")
musicOff = pygame.image.load(".\\Sprites\\GameSprites\\musicOff.png")
sfxOn = pygame.image.load(".\\Sprites\\GameSprites\\sfxOn.png")
sfxOff = pygame.image.load(".\\Sprites\\GameSprites\\sfxOff.png")
playSprite = pygame.image.load(".\\Sprites\\GameSprites\\playSmall.png")
backSprite = pygame.image.load(".\\Sprites\\GameSprites\\back.png")

def settingsRun(display, fps, header):
    header = pygame.transform.scale_by(header, 2)
    global musicT, sfxT
    while(True):
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
        
        #music
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if musicR.collidepoint(mouseCoord):
                musicT = Toggle.musicToggle(musicT)
                print("music toggled")
        
        #sfx
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if sfxR.collidepoint(mouseCoord):
                sfxT = Toggle.sfxToggle(sfxT)
                print("sfx toggled")
        
        #play
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if playR.collidepoint(mouseCoord):      #start game
                print("start game")
                Game.gameRun(display, fps)
                return
        
        #back
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if backR.collidepoint(mouseCoord):      #return to main menu
                print("return to main")
                return
        
        #display sprites and update display
        Toggle.showBackground(display)
        if musicT:
            display.blit(musicOn, (125, 250))
        else:
            display.blit(musicOff, (125, 250))
        if sfxT:
            display.blit(sfxOn, (375, 250))
        else:
            display.blit(sfxOff, (375, 250))
        display.blit(playSprite, (100, 788))
        display.blit(backSprite, (425, 788))
        display.blit(header, (0,0))
        pygame.display.update()
        fps.tick(30)
