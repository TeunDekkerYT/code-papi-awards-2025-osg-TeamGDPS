import pygame
from gpiozero import Button
vragen = [" " ]
but1 = Button(21)
but2 = Button(20)
but3 = Button(26)
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("yes")
running = True
while running:
    screen.fill((0,0,0))
    if but1.is_pressed == True:
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(0,0,5000,5000))
    if but2.is_pressed == True:
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(0,0,5000,5000))
    if but3.is_pressed == True:
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(0,0,5000,5000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()