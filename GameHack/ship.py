from PIL import Image
import random
import weapons

current_ship = {}
# race = gulfer, shaad, human
# alignment = pirate, neutral, ally
# type = scout(more speed, low hull), cargo(more energy and cargo, only stungun), fighter(forcage boosts, only rockets)
def current_ship_generator(type, race, alignment):
    weapons.weapon_generator()
    if race == "gulfer":
        leha = ("gulfer_ship.png")
    elif race == "shaad":
        leha = ("shaad_ship.png")
    elif race == "human":
        leha = ("human_ship.png")
    pic = Image.open(leha).convert('RGBA')
    pixels = pic.load()
    for i in range(pic.width):
        for j in range(pic.height):
            r, g, b, a = pixels[i, j]
            if r == 0 and g == 0 and b == 0:
                if alignment == "pirate":
                    r = 255
                    g = 50
                    b = 50
                if alignment == "ally":
                    r = 50
                    g = 255
                    b = 50
                if alignment == "neutral":
                    r = 100
                    g = 100
                    b = 150
            if r == 255 and g == 255 and b == 255:
                a = 0
            pixels[i, j] = r, g, b, a
    leha = "current_ship.png"
    pic.save(leha)
    if type == "scout":
        global current_ship
        current_ship= {
            'picture': leha,
            'hull': 20,
            'max_hull': 20,
            'speed': 0,  # 40%
            'max_speed': 40,
            'shields': 0,
            'max_shields': 1,
            'reactor': 0,
            'max_reactor': 3,
            'weapon1': {
                'name': "double blaster",
                'ion': False,
                'projectile': "energy",  # ray, rocket
                'power_usage': 1,
                'rocket_usage': 0,
                'shots': 2,
                'damage': 1
            },
            'weapon2': None,
            'oxygen': 80,
            'max_oxygen': 80,
            'size': 1,
            'fuel': 10,
            'ammo': 0,
            'cargo': {'кофе': 0,
                      'варп кристаллы': 0,
                      'пряность': 0},
            'credit': 20
        }
    elif type == "cargo":
        global current_ship
        current_ship = {
            'picture': leha,
            'hull': 35,
            'max_hull': 35,
            'speed': 0,
            'max_speed': 15,  # 40%
            'shields': 0,
            'max_shields': 1,
            'reactor': 0,
            'max_reactor': 5,
            'weapon1': {
                'name': "ion gun",
                'ion': True,
                'projectile': "energy",  # ray, rocket
                'power_usage': 1,
                'rocket_usage': 0,
                'shots': 1,
                'damage': 2
            },
            'weapon2': None,
            'oxygen': 120,
            'max_oxygen': 120,
            'size': 3,
            'fuel': 20,
            'ammo': 5,
            'cargo': {'кофе': 0,
                      'варп кристаллы': 0,
                      'пряность': 0},
            'credit': 30
        }
    elif type == "fighter":
        global current_ship
        current_ship = {
            'picture': leha,
            'hull': 30,
            'max_hull': 30,
            'speed': 0,
            'max_speed': 20,  # 40%
            'shields': 0,
            'max_shields': 1,
            'reactor': 0,
            'max_reactor': 3,
            'weapon1': {
                'name': "rocketlauncher Artemis",
                'ion': False,
                'projectile': "rocket",  # ray, energy
                'power_usage': 1,
                'rocket_usage': 1,
                'shots': 1,
                'damage': 1
            },
            'weapon2': None,
            'oxygen': 180,
            'max_oxygen': 100,
            'size': 2,
            'fuel': 10,
            'ammo': 15,
            'cargo': {'кофе': 0,
                      'варп кристаллы': 0,
                      'пряность': 0},
            'credit': 20
        }
    return pic


def oppose_ship_generator(type, race, alignment):
    weapons.weapon_generator()
    if race == "gulfer":
        leha = ("gulfer_ship.png")
    elif race == "shaad":
        leha = ("shaad_ship.png")
    elif race == "human":
        leha = ("human_ship.png")
    pic = Image.open(leha).ROTATE_180.convert('RGBA')
    pixels = pic.load()
    for i in range(pic.width):
        for j in range(pic.height):
            r, g, b, a = pixels[i, j]
            if r == 0 and g == 0 and b == 0:
                if alignment == "pirate":
                    r = 255
                    g = 10
                    b = 10
                if alignment == "ally":
                    r = 10
                    g = 255
                    b = 10
                if alignment == "neutral":
                    r = 100
                    g = 100
                    b = 150
            if r == 255 and g == 255 and b == 255:
                a = 0
            pixels[i, j] = r, g, b, a
    leha = "oppose_ship.png"
    pic.save(leha)
    rand_num = random.randint(-10, 10)
    if type == "scout":
        oppose_ship = {
            'picture': leha,
            'hull': 20,
            'max_hull': (20 + rand_num) / 2,
            'speed': 0,
            'max_speed': 40 + rand_num,  # 40%
            'shields': 0,
            'max_shields': 1 + random.randint(-1, 2),
            'reactor': 0,
            'max_reactor': 3 + random.randint(-1, 2),
            'weapon1': weapons.weapon1,
            'weapon2': weapons.weapon2,
            'oxygen': 80,
            'max_oxygen': 80,
            'size': 1 + random.randint(-1, 1),
            'fuel': 10 + rand_num,
            'ammo': 0 + rand_num,
            'cargo': {'кофе': random.randint(0, 3),
                      'варп кристаллы': random.randint(0, 10),
                      'пряность': random.randint(0, 2)},
            'credit': 10 + rand_num // 2
        }
        oppose_ship['hull'] = oppose_ship['max_hull']
    elif type == "cargo":
        oppose_ship = {
            'picture': leha,
            'hull': 35,
            'max_hull': (35 + rand_num) / 2,
            'speed': 0,
            'max_speed': 15 + rand_num,  # 40%
            'shields': 0,
            'max_shields': 1 + random.randint(-1, 2),
            'reactor': 0,
            'max_reactor': 5 + random.randint(-1, 2),
            'weapon1': weapons.weapon1,
            'weapon2': weapons.weapon2,
            'oxygen': 120,
            'max_oxygen': 120,
            'size': 3 + random.randint(-1, 1),
            'fuel': 20 + rand_num,
            'ammo': 5 + rand_num,
            'cargo': {'кофе': random.randint(0, 15),
                      'варп кристаллы': random.randint(0, 10),
                      'пряность': random.randint(0, 15)},
            'credit': 20 + rand_num // 2
        }
        oppose_ship['hull'] = oppose_ship['max_hull']
    elif type == "fighter":
        oppose_ship = {
            'picture': leha,
            'hull': 30,
            'max_hull': (30 + rand_num) / 2,
            'speed': 0,
            'max_speed': 20 + rand_num,  # 40%
            'shields': 0,
            'max_shields': 2 + random.randint(-1, 2),
            'reactor': 0,
            'max_reactor': 3 + random.randint(-1, 2),
            'weapon1': weapons.weapon1,
            'weapon2': weapons.weapon2,
            'oxygen': 100,
            'max_oxygen': 100,
            'size': 2 + random.randint(-1, 1),
            'fuel': 10 + rand_num,
            'ammo': 15 + rand_num,
            'cargo': {'кофе': random.randint(0, 3),
                      'варп кристаллы': random.randint(0, 5),
                      'пряность': random.randint(0, 2)},
            'credit': 15 + rand_num // 2
        }
        oppose_ship['hull'] = oppose_ship['max_hull']
    return oppose_ship, pic

def space_station_generator(race, alignment):
    weapons.weapon_generator()
    if race == "gulfer":
        leha = ("gulfer_station.png")
    elif race == "shaad":
        leha = ("shaad_station.png")
    elif race == "human":
        leha = ("human_station.png")
    pic = Image.open(leha).convert('RGBA')
    pixels = pic.load()
    for i in range(pic.width):
        for j in range(pic.height):
            r, g, b, a = pixels[i, j]
            if r == 0 and g == 0 and b == 0:
                if alignment == "pirate":
                    r = 255
                    g = 10
                    b = 10
                if alignment == "ally":
                    r = 10
                    g = 255
                    b = 10
                if alignment == "neutral":
                    r = 100
                    g = 100
                    b = 150
            if r == 255 and g == 255 and b == 255:
                a = 0
            pixels[i, j] = r, g, b, a
    leha = "space_station.png"
    pic.save(leha)
    rand_num = random.randint(-10, 10)

    space_station = {
        'picture': leha,
        'hull': 35,
        'max_hull': (35 + rand_num) * 2,
        'speed': 0,
        'max_speed': 0,  # 40%
        'shields': 0,
        'max_shields': 3 + random.randint(-1, 3),
        'reactor': 0,
        'max_reactor': 6 + random.randint(-1, 3),
        'weapon1': weapons.weapon_statioanary,
        'weapon2': weapons.weapon_statioanary_support,
        'oxygen': 99999,
        'max_oxygen': 99999,
        'size': 5,
        'fuel': 40 + rand_num,
        'ammo': 30 + rand_num,
        'cargo': {'кофе': random.randint(0, 100),
                  'варп кристаллы': random.randint(0, 100),
                  'пряность': random.randint(0, 80)},
        'credit': 100 + rand_num
        }
    space_station['hull'] = space_station['max_hull']
    return space_station