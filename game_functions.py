#coding=utf-8
import sys
import pygame

def check_events():
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """更新屏幕的图像，并切换到新屏幕"""    
    # 每次循环时候都重绘屏幕
    screen.fill(ai_settings.bg_color)        
    ship.blitme()
            
    # 让最近绘制的屏幕可见
    pygame.display.flip()
