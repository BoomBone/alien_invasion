import pygame
import sys

from settings import Settings
from ship import Ship
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
    # 创建一个用于存储子弹的编组
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次循环时都重绘屏幕
        ship.update()
        bullets.update()
        gf.update_screeen(ai_settings, screen, ship, bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
