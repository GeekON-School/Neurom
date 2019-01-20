import pygame
from pygame.locals import *
import random
import sys
import os

WIDTH = 1024
HEIGHT = 786  
SIZE = 50
AST_TIME = 1000
AST_SPEED = -3
AST_SIZE = 90
COIN_SPEED = -3
SHIP_SPEED = 3.75
SHIP_SIZE=[1,1]
ASTEROID_SIZE=[1,1]
COIN_SIZE=[1,1]


# экран смерти
def death():
    pygame.quit()
    sys.exit()


# фон
def set_bg():
    return (pygame.image.load("background.png").convert())


# дисплей
def set_display(bg):

    DISPLAY.fill((0, 0, 0))
    DISPLAY.blit(bg, [0, 0])


# отображение героя
def set_hero(x, y):
    hero_rect = pygame.Rect(x, y, SIZE, SIZE)
    hero_surf = pygame.transform.scale(IMG, (SIZE * 2, SIZE * 2))
    DISPLAY.blit(hero_surf, hero_rect)
    return hero_rect


# проверка на соприкосновение с границами экрана
def check_border(x, y,xspeed,yspeed,width,height):
    if x <=45:
        xspeed=0
        x=50
    if x>=width-45:
        x=width-50
        xspeed=0
    if y <=45:
        yspeed=0
        y=50
    if y>=height-45:
        yspeed=0
        y=height-50
    return x, y,xspeed,yspeed


# проверка на соприкосновение с астероидами и монетками
def check_clash(score, asteroids, coin, hero):
    if hero.colliderect(coin):
        score += 1
        coin = None
    if hero.collidelist(asteroids) != -1:
        death()
        sys.exit()
    return score, coin


# расположение астероидов
def set_asteroids(asteroids, buf_time):
    if ((pygame.time.get_ticks() - buf_time) > AST_TIME):
        ast = pygame.Rect(WIDTH, random.randint(0, HEIGHT - AST_SIZE), AST_SIZE, AST_SIZE)
        asteroids.append(ast)
        buf_time = pygame.time.get_ticks()
    for itr in asteroids:
        itr.move_ip(AST_SPEED, 0)
        ast_surf = pygame.transform.scale(AST_IMG, (AST_SIZE, AST_SIZE))
        DISPLAY.blit(ast_surf, itr)
        if itr.x < AST_SIZE * (-1):
            asteroids.remove(itr)
    return buf_time


# расположение монет
def set_coin(coin):
    if (coin == None):
        coin = pygame.Rect(WIDTH + SIZE, random.randint(SIZE, HEIGHT - SIZE), SIZE, SIZE)
    if (coin.x == 0 - SIZE * 2):
        coin.move_ip(WIDTH, random.randint(SIZE, HEIGHT - SIZE))
    coin.move_ip(COIN_SPEED, 0)
    coin_surf = pygame.transform.scale(COIN_IMG, (SIZE, SIZE))
    DISPLAY.blit(coin_surf, coin)
    return coin


# проверка на движение
def move(event, x_speed, y_speed):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            x_speed = -SHIP_SPEED
        if event.key == pygame.K_d:
            x_speed = SHIP_SPEED
        if event.key == pygame.K_w:
            y_speed = -SHIP_SPEED
        if event.key == pygame.K_s:
            y_speed = SHIP_SPEED
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            x_speed = 0
        if event.key == pygame.K_d:
            x_speed = 0
        if event.key == pygame.K_w:
            y_speed = 0
        if event.key == pygame.K_s:
            y_speed = 0
    return x_speed, y_speed


# запуск игры
def rungame():
    x = 56
    y = 240
    x_speed = 0
    y_speed = 0
    sound1 = pygame.mixer.Sound('music.ogg')
    sound1.play()
    background = set_bg()
    score = 0
    asteroids = []
    coin = None
    buf_time = pygame.time.get_ticks()
    while True:
        set_display(background)
        hero = set_hero(x, y)
        buf_time = set_asteroids(asteroids, buf_time)
        coin = set_coin(coin)
        
        for event in pygame.event.get():
            x_speed, y_speed = move(event, x_speed, y_speed)
            if event.type == pygame.QUIT:
                return
        score, coin = check_clash(score, asteroids, coin, hero)
        x, y,x_speed,y_speed= check_border(x, y,x_speed,y_speed,WIDTH,HEIGHT)
        x += x_speed
        y += y_speed
        pygame.display.update()
        #FPS
        pygame.time.delay(10)


# исходная функция
def main():
    global DISPLAY, IMG, FONT_POINTS, FONT_TIME, START_TIME, AST_IMG, COIN_IMG
    pygame.init()
    # path = os.path.join(os.getcwd(), 'freesansbold.ttf')
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    IMG = pygame.image.load("spaceshipone.png")
    rot = pygame.transform.rotate(IMG, 90)
    rot_rect = rot.get_rect(center=(200, 150))
    AST_IMG = pygame.image.load("asteroid.png")
    COIN_IMG = pygame.image.load("coin.png")
    START_TIME = pygame.time.get_ticks()
    rungame()
    pygame.quit()


main()
sys.exit(0)
