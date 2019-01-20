import ship
import ship_encounter
import talk
import random
import talk
#если выберут окно переговоров
while True: #senya
    button1 = random.choice(["hull repair", "talk"])
    button2 = random.choice(["fuel shop", "talk"])
    button3 = random.choice(["ammo shop", "talk"])
    #если есть магазин
    button4 = "weapon_shop"
    button5 = random.choice(["weapon_shop", "talk", "weapon_shop", "talk", "weapon_shop", "talk", "coffe_shop", "crystal_shop", "spice_shop"])
    #если нет
    button4 = "talk"
    button5 = "talk"
    #если есть квест
    button6 = "request"
    #если нет
    button6 = "talk"

    enter = input()

    if enter == "w" or enter == "a" or enter == "s" or enter == "d":
        break
    elif enter == " ":
        if button1 == "talk":
            frase = talk.frase_generator()
        elif button1 == "hull repair":
            frase = talk.frase_generator()
            price = talk.price
    elif enter == "e":
        if button2 == "talk":
            frase = talk.frase_generator()
        elif button2 == "fuel shop":
            frase = talk.frase_generator()
            price = talk.price
    elif enter == "f":
        if button3 == "talk":
            frase = talk.frase_generator()
        elif button3 == "ammo shop":
            frase = talk.frase_generator()
            price = talk.price
    elif enter == "q":
        price = talk.price
    elif enter == "r":
        if button5 == "talk":
            frase = talk.frase_generator()
        elif button5 == "coffe_shop":
            frase = talk.frase_generator()
            price = talk.price
        elif button5 == "crystal_shop":
            frase = talk.frase_generator()
            price = talk.price
        elif button5 == "spice_shop":
            frase = talk.frase_generator()
            price = talk.price
    elif enter == "z":
        if button6 == "talk":
            frase = talk.frase_generator()
        elif button6 == "request":
            frase = talk.frase_generator()
            price = talk.price



