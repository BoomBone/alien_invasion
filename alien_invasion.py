import pygame
import sys

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
