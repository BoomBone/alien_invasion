import pygame
import sys

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次循环时都重绘屏幕
        ship.update()
        gf.upadte_bullets(bullets)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()
