#imports
import pygame
pygame.init()
import random
import time
from gpiozero import Button
import math
#vragen + antwoorden vars
vragen = ["als iemand je adress vraagt geef je hem dan","als mensen gegevens vragen zoals je ip geef je het dan","als mensen je pesten pest je ze dan terug","wat moet je beter niet doen met cyberpesten","hoe kun je cyberpesten helpen voorkomen","wat kan je doen als iemand anders gepest wordt","wat kun je doen als het pesten door blijft gaan","wat is online respect","is cyberpesten strafbaar?","wat betekent digitale weerbaarheid","wat is goed bewijs van cyberpesten","wie kan je helpen bij cyberpesten","waarom is cyberpesten extra vervelend","welke situatie is cyberpesten","wat betekent iemand blokkeren"]
antwoord_a = ["ja","ja","ja","terug pesten","sterke wachtwoorden gebruiken","meedoen","extra hulp inschakelen","aardig zijn tegen anderen","ja","jezelf online kunnen beschermen","screenshots van berichten maken","een docent of ouder","het kan altijd door blijven gaan","iemand uitschelden via social media","dat iemand je geen berichten meer kan sturen"]
antwoord_b = ["nee","nee","nee","hulp vragen","alles openbaar delen","steun geven en melden","stoppen met internet","zeggen wat je wilt","nee","veel volgers hebben","geruchten","niemand","het gebeurt maar 1 keer","een foto liken","iemand volgen"]
antwoord_c = ["ligt aan de situatie","ligt aan de situatie","ja erger","bewijs bewaren","verkeerde informatie geven","niets doen","niets","mensen uitsluiten","alleen op school","altijd online zijn","likes","alleen vrienden online","het is niet erg","chatten met vrienden","iemand offline pesten"]
goed_antwoord = ["ligt aan de situatie","nee","nee","terug pesten","sterke wachtwoorden gebruiken","steun geven en melden","extra hulp inschakelen","aardig zijn tegen anderen","ja","jezelf online kunnen beschermen","screenshots van berichten maken","een docent of ouder","het kan altijd door blijven gaan","iemand uitschelden via social media","dat iemand je geen berichten meer kan sturen"]
tot_vragen = 15
awnser:str
good:int
hoeveel_goed = 0
a_ran:int
b_ran:int
c_ran:int
a = ""
b = ""
c = ""
rand:int
preparing = True
#buttons
but1 = Button(21)
but2 = Button(20)
but3 = Button(26)
pressed = False
#dimensions scherm zodat niet kaboem

SCREEN_WIDTH = 1920
SCREEN_LENGHT = 1080

#das screen

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_LENGHT))
imp = pygame.image.load("green_cube.png").convert()
#vars
player = pygame.Rect((300,250,1,1))
SPEED = 10
B = 0
A = 0
right = False
wrong = False
#pos van vierkanten
pos1x = random.randint(10,1500)
pos2x = random.randint(10,1500)
pos3x = random.randint(10,1500)
pos4x = random.randint(10,1500)
pos5x = random.randint(10,1500)
pos6x = random.randint(10,1500)
pos7x = random.randint(10,1500)
pos1y = random.randint(0,800)
pos2y = random.randint(0,800)
pos3y = random.randint(0,800)
pos4y = random.randint(0,800)
pos5y = random.randint(0,800)
pos6y = random.randint(0,800)
pos7y = random.randint(0,800)
#text vars
font = "PixelPurl.ttf"
text_color = (135.6,255,0)
#vierkanten
image1 = pygame.image.load("green_cube.png")
imrect1 = image1.get_rect()
angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0
angle5 = 0
angle6 = 0
angle7 = 0
rotate1 = random.randint(3,6)
rotate2 = random.randint(3,6)
rotate3 = random.randint(3,6)
rotate4 = random.randint(3,6)
rotate5 = random.randint(3,6)
rotate6 = random.randint(3,6)
rotate7 = random.randint(3,6)
size1 = random.randint(50,450)
size2 = random.randint(50,450)
size3 = random.randint(50,450)
size4 = random.randint(50,450)
size5 = random.randint(50,450)
size6 = random.randint(50,450)
size7 = random.randint(50,450)
image1.set_alpha(40)
#geluid af spelen
def sound(what_sound):
    pygame.mixer.init()
    pygame.mixer.Sound(what_sound)
    pygame.mixer.Sound(what_sound).play().set_volume(1)
#het vragen algoritme
def prepare():
    global rand
    global a
    global b
    global c
    preparing = False
    rand = random.randint(0,tot_vragen - 1)
    vraag = vragen[rand]
    a_ran = random.randint(1,3)
    c_ran = random.randint(1,3)
    b_ran = random.randint(1,3)
    if a_ran == b_ran or b_ran == c_ran or a_ran == c_ran:
        print("again")
        prepare()
    else:
        print(a_ran)
        print(b_ran)
        print(c_ran)
        if a_ran == 1:
            a = antwoord_a[rand]
        elif a_ran == 2:
            a = antwoord_b[rand]
        elif a_ran == 3:
            a = antwoord_c[rand]
        
        if b_ran == 1:
            b = antwoord_a[rand]
        elif b_ran == 2:
            b = antwoord_b[rand]
        elif b_ran == 3:
            b = antwoord_c[rand]
        
        if c_ran == 1:
            c = antwoord_a[rand]
        elif c_ran == 2:
            c = antwoord_b[rand]
        elif c_ran == 3:
            c = antwoord_c[rand]
        print(a)
        print(b)
        print(c)
        print(rand)
        pass
screen.blit(imp,(0,0))
run = True
#de loop
while run:
    screen.fill((0,0,0))
    #zorgt dat hij prepare doet
    if preparing == True:
        prepare()
        preparing = False
    else:
        
        #dit is voor de b knop
        if but3.is_pressed:
            if not pressed:
                if goed_antwoord[rand] == b:
                    print("yes")
                    right = True
                    sound("goed.wav")
                    preparing = True
                    pressed = True
                    
                else:
                    print("fuck")
                    print(a)
                    wrong = True
                    sound("fout.wav")
                    preparing = True
                    pressed = True
        
        
        
        #dit is voor de c knop
        if but2.is_pressed:
            if not pressed:
                if goed_antwoord[rand] == c:
                    print("yes")
                    right = True
                    sound("goed.wav")
                    preparing = True
                    pressed = True
                    
                else:
                    print("fuck")
                    print(b)
                    sound("fout.wav")
                    wrong = True
                    preparing = True
                    pressed = True
        
        
        
        
        
        #dit is voor de a knop
        if but1.is_pressed:
            if not pressed:
                if goed_antwoord[rand] == a:
                    print("yes")
                    sound("goed.wav")
                    right = True
                    preparing = True
                    pressed = True
                    
                    
                else:
                    print("fuck")
                    print(c)
                    sound("fout.wav")
                    preparing = True
                    pressed = True
                    wrong = True
            #zodat je niet de knop ingedrukt kan houden en dat hij constant blijft antwoorden
        if not but1.is_pressed and not but2.is_pressed and not but3.is_pressed:
            pressed = False
    #load de vierkante
    rotated_im1 = pygame.transform.rotate(image1,angle1)
    screen.blit(pygame.transform.scale(rotated_im1,(size1,size1)), (pos1x,pos1y))
    angle1 += rotate1
    
    rotated_im1 = pygame.transform.rotate(image1,angle2)
    screen.blit(pygame.transform.scale(rotated_im1,(size2,size2)), (pos2x,pos2y))
    angle2 += rotate2
    
    rotated_im1 = pygame.transform.rotate(image1,angle3)
    screen.blit(pygame.transform.scale(rotated_im1,(size3,size3)), (pos3x,pos3y))
    angle3 += rotate3

    rotated_im1 = pygame.transform.rotate(image1,angle4)
    screen.blit(pygame.transform.scale(rotated_im1,(size4,size4)), (pos4x,pos4y))
    angle4 += rotate4
    
    rotated_im1 = pygame.transform.rotate(image1,angle4)
    screen.blit(pygame.transform.scale(rotated_im1,(size5,size5)), (pos5x,pos5y))
    angle5 += rotate5
    
    rotated_im1 = pygame.transform.rotate(image1,angle6)
    screen.blit(pygame.transform.scale(rotated_im1,(size6,size6)), (pos6x,pos6y))
    angle6 += rotate6
    
    rotated_im1 = pygame.transform.rotate(image1,angle7)
    screen.blit(pygame.transform.scale(rotated_im1,(size7,size7)), (pos7x,pos7y))
    angle7 += rotate7
    #zorgt voor de text
    my_font = pygame.font.Font(font, 70)
    text_surface = my_font.render(a, False, text_color)
    x = 960
    y = 500
    width1,height1 = my_font.size(a)
    x = x-(width1/2)
    y = y-(height1/2)
    screen.blit(text_surface,(x,y))
    
    
    my_font = pygame.font.Font(font, 70)
    text_surface = my_font.render(b, False, text_color)
    x = 960
    y = 600
    width1,height1 = my_font.size(b)
    x = x-(width1/2)
    y = y-(height1/2)
    screen.blit(text_surface,(x,y))
    
    
    my_font = pygame.font.Font(font, 70)
    text_surface = my_font.render(c, False, text_color)
    x = 960
    y = 700
    width1,height1 = my_font.size(c)
    x = x-(width1/2)
    y = y-(height1/2)
    screen.blit(text_surface,(x,y))
    
    
    my_font = pygame.font.Font(font, 100)
    text_surface = my_font.render(vragen[rand], False, text_color)
    x = 960
    y = 200
    width1,height1 = my_font.size(vragen[rand] )
    x = x-(width1/2)
    y = y-(height1/2)
    screen.blit(text_surface,(x,y))
    #rotatie van vierkanten en groote veranderingen 
    if right == True:
        angle1 = 0
        angle2 = 0
        angle3 = 0
        angle4 = 0
        angle5 = 0
        angle6 = 0
        angle7 = 0
        rotate1 = random.randint(3,6)
        rotate2 = random.randint(3,6)
        rotate3 = random.randint(3,6)
        rotate4 = random.randint(3,6)
        rotate5 = random.randint(3,6)
        rotate6 = random.randint(3,6)
        rotate7 = random.randint(3,6)
        size1 = random.randint(50,450)
        size2 = random.randint(50,450)
        size3 = random.randint(50,450)
        size4 = random.randint(50,450)
        size5 = random.randint(50,450)
        size6 = random.randint(50,450)
        size7 = random.randint(50,450)
        pos1x = random.randint(10,1500)
        pos2x = random.randint(10,1500)
        pos3x = random.randint(10,1500)
        pos4x = random.randint(10,1500)
        pos5x = random.randint(10,1500)
        pos6x = random.randint(10,1500)
        pos7x = random.randint(10,1500)
        pos1y = random.randint(0,800)
        pos2y = random.randint(0,800)
        pos3y = random.randint(0,800)
        pos4y = random.randint(0,800)
        pos5y = random.randint(0,800)
        pos6y = random.randint(0,800)
        pos7y = random.randint(0,800)
        screen.fill((0,255,0))
        pygame.display.update()
        time.sleep(0.15)
        right = False
    if wrong == True:
        angle1 = 0
        angle2 = 0
        angle3 = 0
        angle4 = 0
        angle5 = 0
        angle6 = 0
        angle7 = 0
        rotate1 = random.randint(3,6)
        rotate2 = random.randint(3,6)
        rotate3 = random.randint(3,6)
        rotate4 = random.randint(3,6)
        rotate5 = random.randint(3,6)
        rotate6 = random.randint(3,6)
        rotate7 = random.randint(3,6)
        size1 = random.randint(50,450)
        size2 = random.randint(50,450)
        size3 = random.randint(50,450)
        size4 = random.randint(50,450)
        size5 = random.randint(50,450)
        size6 = random.randint(50,450)
        size7 = random.randint(50,450)
        pos1x = random.randint(10,1500)
        pos2x = random.randint(10,1500)
        pos3x = random.randint(10,1500)
        pos4x = random.randint(10,1500)
        pos5x = random.randint(10,1500)
        pos6x = random.randint(10,1500)
        pos7x = random.randint(10,1500)
        pos1y = random.randint(0,800)
        pos2y = random.randint(0,800)
        pos3y = random.randint(0,800)
        pos4y = random.randint(0,800)
        pos5y = random.randint(0,800)
        pos6y = random.randint(0,800)
        pos7y = random.randint(0,800)
        screen.fill((255,0,0))
        pygame.display.update()
        time.sleep(0.15)
        wrong = False
    #makes it so you can fcking quit life and die
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            print("quiting")
            
    pygame.display.update()
#zorgt dat de window sluit
pygame.quit()
print("heb je al een keer gehoort van de godot particle system de perfecte manier om particles te maken en je levensproblemen op te lossen nu verkrijgbaar op de godot game engine de perfecte manier om games te maken en levensproblemen te krijgen?")
print("quit succesfully done")