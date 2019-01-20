import random
import weapons
import ship

def name_generator():
    name = "the " + random.choice(["White ", "Golden ", "Black ", "Royal ", "Red ", "Elite "]) + random.choice(["String ", "Sun ", "Star ", "Horse ", "Hound "]) + random.choice(["club", "bar", "cafe", "pub"])
    return name
def frase_generator():
    name = name_generator()
    frase = random.choice([f'''Перед вами заведение с вывеской {name}. Охранник сообщает, что вход только по пропускам''',
                           f'''Перед вами заведение с вывеской {name}. На двери весит табличка "закрыто"''',
                           f'''Перед вами заведение с вывеской {name}.
Охранник сообщает, что вход представителям вашей расы воспрещён''',
                           f'''На лавочке перед вами скучает сомнительного вида незнакомец. 
Заметив вас он предлагает вам посетить вместе с ним {name}, но вы отказываетесь''',
                           f'''На лавочке перед вами скучает сомнительного вида незнакомец. 
Заметив вас он говорит вам не ходить в {name} и начинает жаловаться вам на жизнь.''',
                           ])
    return frase
price = random.randint(20, 50)
def weapon_shop(price): #asad
    weapons.weapon_generator()
    weapon_for_sale = weapons.weapon1
    return price, weapon_for_sale
def hull_repair(price):

    if ship.current_ship['credits'] >= 3 and ship.current_ship['hull'] < ship.current_ship['max_hull']:
        price = 3
        ship.current_ship['credits'] -= 3
        ship.current_ship['hull'] += 1
    return price
def fuel_shop(price):

    if ship.current_ship['credits'] >= 2:
        price = 2
        ship.current_ship['credits'] -= 2
        ship.current_ship['fuel'] += 1
    return price
def ammo_shop(price):

    if ship.current_ship['credits'] >= 5:
        price = 5
        ship.current_ship['credits'] -= 5
        ship.current_ship['ammo'] += 1
    return price
def coffe_shop(price):
    price = price // 2
    if ship.current_ship['credits'] >= price:
        ship.current_ship['credits'] -= price
        ship.current_ship['cargo']['кофе'] += 1
def crystal_shop(price):
    price = price // 2
    if ship.current_ship['credits'] >= price:
        ship.current_ship['credits'] -= price
        ship.current_ship['cargo']['варп кристаллы'] += 1
def spice_shop(price):
    price = price // 2
    if ship.current_ship['credits'] >= price:
        ship.current_ship['credits'] -= price
        ship.current_ship['cargo']['пряность'] += 1
def request_generator():

    while request != "a" or request != "d":
        resource = random.choice(['кофе', 'варп кристаллов', 'пряности'])
        ammount = random.choice
        request = input(f"""Вы осматриваете окрестности, как вдруг вас подзывают:
 - Эй, ты! Да, ты, я ищу {ammount}т {resource}. Если утебя найдётся столько, я щедро заплачу.""")