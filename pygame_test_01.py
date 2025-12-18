import pygame
pygame.init()

#dimensions screen

SCREEN_WIDTH = 1200
SCREEN_LENGHT = 800

#das screen

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_LENGHT))

#vars
player = pygame.Rect((300,250,1,1))
SPEED = 10
B = 0
A = 0
#loop

run = True
while run:
    
    screen.fill((50,0,80))
    
    my_font = pygame.font.SysFont('Comic_Sans', 70)
    text_surface = my_font.render('C', True, (255,0,255))
    screen.blit(text_surface,(1000,600))
    my_font = pygame.font.SysFont('Papyrus', 70)
    text_surface = my_font.render('B', True, (0,255,255))
    screen.blit(text_surface,(600,600))
    my_font = pygame.font.SysFont('Papyrus', 70)
    text_surface = my_font.render('A', True, (255,255,0))
    screen.blit(text_surface,(200,600))
    my_font = pygame.font.SysFont('Papyrus', 100)
    text_surface = my_font.render('VRAAG TEKST', True, (0,0,255))
    text_surface.get_rect().center = (text_surface.get_rect().height / 2,text_surface.get_rect().width / 2)
    screen.blit(text_surface,(600,200))
    
    pygame.draw.rect(screen, (255,255,255), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-SPEED,0)
    elif key[pygame.K_d] == True:
        player.move_ip(SPEED,0)
    if key[pygame.K_w] == True:
        player.move_ip(0,-SPEED)
    elif key[pygame.K_s] == True:
        player.move_ip(0,SPEED)

    #makes it so you can fcking quit life and die
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("quiting")
            
    pygame.display.update()

pygame.quit()
print("quit succesfully done")