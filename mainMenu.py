import pygame, Toggle
Toggle.startUp()        #load default settings
import Game, Customization, Settings  #Additional files/menus
pygame.init()

Display = pygame.display.set_mode((600,900))
pygame.display.set_caption("Adrian's crappy version of Flappy Bird") 
fps = pygame.time.Clock()

#setup 
mode = 0
playR = pygame.Rect((150, 150), (300, 200))
playSprite = pygame.image.load(".\\Sprites\\GameSprites\\play.png")
customizationR = pygame.Rect((150, 400), (300, 75))
customizationSprite = pygame.image.load(".\\Sprites\\GameSprites\\customization.png")
settingsR = pygame.Rect((150, 525), (300, 75))
settingsSprite = pygame.image.load(".\\Sprites\\GameSprites\\settings.png")
resetR = pygame.Rect((225, 775), (150, 75))
resetSprite = pygame.image.load(".\\Sprites\\GameSprites\\reset.png")

while(True):    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):       #handles QUIT anytime
            print("exiting")
            Toggle.quitGame()
        #start game with space
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            print ("playing")  
            Game.gameRun(Display, fps)
        elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_p)): 
            print(Toggle.saveData)
            Toggle.gameUpdate()
        pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION))
         
    mode = 0
    mouseCoord = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
    
    #play button
    if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
        if playR.collidepoint(mouseCoord):
            print ("playing")  
            Game.gameRun(Display, fps)      
        
    #customization button
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if customizationR.collidepoint(mouseCoord):
            print ("customs")
            Customization.customizationRun(Display, fps, customizationSprite)
    
    #settings button
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if settingsR.collidepoint(mouseCoord):
            print ("settings")
            Settings.settingsRun(Display, fps, settingsSprite)
    
    #reset button
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if resetR.collidepoint(mouseCoord):
            print ("reset data")
            Toggle.resetData()
    
    
    #display sprites and update display
    Toggle.showBackground(Display)
    Display.blit(resetSprite, (225, 775))
    Display.blit(playSprite, (150, 150)) 
    Display.blit(customizationSprite, (150, 400))
    Display.blit(settingsSprite, (150, 525))
    pygame.display.update()
    fps.tick(30)