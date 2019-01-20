import ship
import station
import random
ship.space_station_generator()
ship.oppose_ship_generator()
opponent = ship.oppose_ship() #из карты
#или
opponent = ship.space_station #из карты
battle = "none"
turn = "your" #opponent
"""варианты манёвров:
1 меню действий
    1.1 сдаться щадят если на картинке есть цвет твоей фракции (если кто-то нейтрал, то рандом) -10 кредов, полная зарядка привода Кадора
    1.2 потребовать капитуляции если хп врага <= 10% даёт свои креды и улетает
    1.3 предложить переговоры если на картинке есть цвет твоей фракции остановка боя и если есть квест или станция открывается окно
    1.4 совершить прыжок (только если привод Кадора заряжен)
    1.5 облутать (только если бой закончен) на random.randint(
    1.6 к меню манёвров
2 активация первого оружия
3 активация второго оружия
4 форсаж щитов заряжает все щиты +1 дополнительный (за каждый щит -1 энергия)
5 форсаж движков -вся энергия но за каждую единицу +уклонение (вплоть до максимума + 10) и +заряд привода Кадора
6[зажать] открыть карту
"""
#если алигнмент противоположен (если нейтрал 50проц) battle = "in_process"
#если атакуешь battle = "in_process"
def maneuver_menu(opponent):
    enter = input()
    if enter == " ":
        action_menu(opponent)
    elif enter == "e":
    elif enter == "f":
    elif enter == "q":
    elif enter == "r":
    elif enter == "z":
    return opponent

def action_menu(opponent):
    enter = input()
    if enter == " ":
        surrender_win(opponent)
    elif enter == "e":
        surrender_lose(opponent)
    elif enter == "f":
        if battle == "lose" or battle == "none"
            open(station)
    elif enter == "q":
    elif enter == "r":
        loot(opponent)
    elif enter == "z":
        maneuver_menu(opponent)
    return opponent

def surrender_lose(opponent):
    return opponent

def surrender_win(opponent):
    return opponent

def loot (opponent):
    ship.current_ship['cargo'] += opponent['cargo']
    ship.current_ship['ammo'] += opponent['ammo'] // 2
    ship.current_ship['fuel'] += opponent['fuel'] // 2
    ship.current_ship['credit'] += opponent['credit'] // 2
    return opponent

def shoot_weapon(opponent):
    battle = "in_process"
    return opponent

def opponent_turn(opponent):
    if battle == "in_process":
        if opponent['max_hull'] // 10 >= opponent['hull']:
            if random.randint(1, 3) > 2:
                surrender_win(opponent)
        elif opponent['shields'] < opponent['max_shields'] and opponent['reactor'] != 0:
            opponent['reactor'] -= 1
            opponent['shields'] += 1
        elif opponent['speed'] < opponent['max_speed'] and opponent['reactor'] != 0:
            opponent['reactor'] -= 1
            opponent['speed'] += 10
        while opponent['reactor'] != 0:
            if opponent['reactor'] >= opponent['weapon1']['power_usage'] and opponent['ammo'] >= opponent['weapon1']['rocket_usage']:
                shoot_weapon(opponent)
            if opponent['reactor'] >= opponent['weapon2']['power_usage'] and opponent['ammo'] >= opponent['weapon2']['rocket_usage']:
                shoot_weapon(opponent)