import random
def weapon_generator():
    weapon1 = random.choice([{
        'name': "double blaster",
        'ion': False,
        'projectile': "energy",  # ray, rocket
        'power_usage': 1,
        'rocket_usage': 0,
        'shots': 2,
        'damage': 1
        }, {
        'name': "ion gun",
        'ion': True,
        'projectile': "energy",  # ray, rocket
        'power_usage': 1,
        'rocket_usage': 0,
        'shots': 1,
        'damage': 2
        }, {
        'name': "rocketlauncher Artemis",
        'ion': False,
        'projectile': "rocket",  # ray, energy
        'power_usage': 1,
        'rocket_usage': 1,
        'shots': 1,
        'damage': 1
    }])
    weapon2 = random.choice([[None] * 7, {
        'name': "double blaster",
        'ion': False,
        'projectile': "energy",  # ray, rocket
        'power_usage': 1,
        'rocket_usage': 0,
        'shots': 2,
        'damage': 1
        }, {
         'name': "ion gun",
         'ion': True,
         'projectile': "energy",  # ray, rocket
         'power_usage': 1,
         'rocket_usage': 0,
         'shots': 1,
         'damage': 2
        }, {
         'name': "rocketlauncher Artemis",
         'ion': False,
         'projectile': "rocket",  # ray, energy
         'power_usage': 1,
         'rocket_usage': 1,
         'shots': 1,
         'damage': 1
        }])
    weapon_statioanary = random.choice([
        {'name': "blaster battery",
         'ion': False,
         'projectile': "energy",  # ray, rocket
         'power_usage': 1,
         'rocket_usage': 0,
         'shots': 6,
         'damage': 1},
        {'name': "ion battery",
         'ion': True,
         'projectile': "energy",  # ray, rocket
         'power_usage': 1,
         'rocket_usage': 0,
         'shots': 10,
         'damage': 1}])
    weapon_statioanary_support = random.choice([{
         'name': "uber blast",
         'ion': False,
         'projectile': "energy",  # ray, rocket
         'power_usage': 0,
         'rocket_usage': 0,
         'shots': 1,
         'damage': 10
        },{
         'name': "ray battery",
         'ion': False,
         'projectile': "ray",  # ray, rocket
         'power_usage': 0,
         'rocket_usage': 0,
         'shots': 2,
         'damage': 3
        },{
         'name': "ion ray",
         'ion': True,
         'projectile': "ray",  # ray, rocket
         'power_usage': 0,
         'rocket_usage': 0,
         'shots': 4,
         'damage': 1
        },{
         'name': "rocketlauncher Vulcan",
         'ion': True,
         'projectile': "ray",  # ray, rocket
         'power_usage': 0,
         'rocket_usage': 3,
         'shots': 5,
         'damage': 2}
        ])
    return weapon_statioanary_support, weapon_statioanary, weapon1, weapon2
