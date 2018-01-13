import sys
import pygame


def check_events(ship):
    """响应按键和鼠标时间"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.key ==pygame.K_RIGHT:
            #向右移动飞船
            ship.rect.centerx+=1


def update_screeen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
