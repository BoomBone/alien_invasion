import pygame
import sys

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(screen)

    while True:
        gf.check_events(ship)
        # 每次循环时都重绘屏幕
        gf.update_screeen(ai_settings, screen, ship)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
