import ship
import simpleaudio
from PIL import Image
print("""
                   _                                       _           
                  | |                                     | |          
__      __   ___  | |   ___    ___    _ __ ___     ___    | |_    ___  
\ \ /\ / /  / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \ 
 \ V  V /  |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |
  \_/\_/    \___| |_|  \___|  \___/  |_| |_| |_|  \___|    \__|  \___/ 
                                                                       
                                                                       """)
sound = simpleaudio.WaveObject.from_wave_file("title.wav")
play_obj = sound.play()
play_obj.wait_done()

print(""" ▐ ▄     ▄▄▄ .    ▄• ▄▌    ▄▄▄                • ▌ ▄ ·. """)
play_obj = sound.play()
play_obj.wait_done()
print("""•█▌▐█    ▀▄.▀·    █▪██▌    ▀▄ █·    ▪         ·██ ▐███▪""")
play_obj = sound.play()
play_obj.wait_done()
print("""▐█▐▐▌    ▐▀▀▪▄    █▌▐█▌    ▐▀▀▄      ▄█▀▄     ▐█ ▌▐▌▐█·""")
play_obj = sound.play()
play_obj.wait_done()
print("""██▐█▌    ▐█▄▄▌    ▐█▄█▌    ▐█•█▌    ▐█▌.▐▌    ██ ██▌▐█▌""")
play_obj = sound.play()
play_obj.wait_done()
print("""▀▀ █▪     ▀▀▀      ▀▀▀     .▀  ▀     ▀█▄▀▪    ▀▀  █▪▀▀▀""")
play_obj = sound.play()
play_obj.wait_done()
while True:
    race = input('''
Вы капитан корабля "Чёрная Звезда", Вы принадлежите к расе 
Шаадов [джойстик вниз]
Людей   [джойстик влево]
Гальферов [джойстик вправо]''')
    if race == "s":
        race = "shaad"
        race_rus = "шаадов"
    elif race == "a":
        race = "human"
        race_rus = "людей"
    elif race == "d":
        race = "gulfer"
        race_rus = "гальферов"
    else:
        print("Вы нажали что-тот не то")
        continue

    alignment = input('''
являясь знаменитым 
Пиратом [джойстик вниз]
Наёмником [джойстик в бок]
Офицером [джойстик вверх]''')

    if alignment == "s":
        alignment = "pirate"
        alignment_rus = "пиратом"
    elif alignment == "a" or alignment == "d":
        alignment = "neutral"
        alignment_rus = "наёмником"
    elif alignment == "w":
        alignment = "ally"
        alignment_rus = "офицером"
    else:
        print("Вы нажали что-тот не то")
        continue
    type = input('''
вы бороздите просторы космоса на своём корабле типа
Разведчик (быстрый, но беззащитный) [джойстик вверх]
Грузовой (тяжёлый корабль с большим складом. Страдает от нехватки огневой мощи) [джойстик в бок]
Исстребитель (мощное судно оснащённое ракетницей) [джойстик вниз]''')
    if type == "s":
        type = "fighter"
        type_rus = "исстребитель"
    elif type == "a" or type == "d":
        type = "cargo"
        type_rus = "грузовой"
    elif type == "w":
        type = "scout"
        type_rus = "разведчик"
    else:
        print("Вы нажали что-тот не то")
        continue
    ship.curent_ship_generator(type, race, alignment)
    accept = input(f"""
Вы капитан корабля "Чёрная Звезда", вы принадлежите к расе {race_rus}, являясь знаменитым {alignment_rus}.
Bы бороздите просторы космоса на своём корабле типа {type_rus}.
[дёрните джойстик для подтверждения, нажмите любую кнопку для отмены]""")
    if accept == "w" or accept == "a" or accept == "s" or accept == "d":
        break
    else:
        continue

#Image.open("current_ship.png").show()
