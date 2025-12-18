from gpiozero import Button
import random
vragen = ["als iemand je om je adres vraagt wat doe je?","ba"]
but1 = Button(21)
but2 = Button(20)
but3 = Button(26)
asking = True
print(vragen[random.randint(0,1)])
ans = 0
while True:
    if ans == 1:
        print("yes")
        ans = 0
    elif ans != 0:
        print("fuck")
        ans = 0
    if asking:
        if but1.is_pressed:
            print("niks")
            ans = 1
            asking = False
        if but2.is_pressed:
            print("ik geef mijn adres")
            ans = 2
            asking = False
        if but3.is_pressed:
            print("ik geef een ander adres")
            ans = 3
            asking = False