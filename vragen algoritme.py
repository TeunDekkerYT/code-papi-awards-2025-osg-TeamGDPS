import random
import time
from gpiozero import Button
vragen = ["a","b","c","d"]
antwoord_a = ["idk","idk","idk","idk"]
antwoord_b = ["nee","nee","nee","nee"]
antwoord_c = ["ja","ja","ja","ja"]
goed_antwoord = ["idk","idk","idk","idk"]
tot_vragen = 4
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
but1 = Button(21)
but2 = Button(20)
but3 = Button(26)
pressed = False
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
while True:
    if preparing == True:
        prepare()
        preparing = False
    else:
        
        #dit is voor de b knop
        if but3.is_pressed:
            if not pressed:
                if goed_antwoord[rand] == b:
                    print("yes")
                    time.sleep(2.5)
                    preparing = True
                    pressed = True
                else:
                    print("fuck")
                    print(a)
                    time.sleep(2.5)
                    preparing = True
                    pressed = True
        
        
        
        #dit is voor de c knop
        if but2.is_pressed:
            if not pressed:
                if goed_antwoord[rand] == c:
                    print("yes")
                    time.sleep(2.5)
                    preparing = True
                    pressed = True
                else:
                    print("fuck")
                    print(b)
                    time.sleep(2.5)
                    preparing = True
                    pressed = True
        
        
        
        
        
        #dit is voor de a knop
        if but1.is_pressed:
            if not pressed:
                if goed_antwoord[rand] == a:
                    print("yes")
                    time.sleep(2.5)
                    preparing = True
                    pressed = True
                else:
                    print("fuck")
                    print(c)
                    time.sleep(2.5)
                    preparing = True
                    pressed = True
        if not but1.is_pressed and not but2.is_pressed and not but3.is_pressed:
            pressed = False
        
    