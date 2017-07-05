#coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion by Jacob")
    
    """创建一只飞船、一个子弹编组、一个外星人编组"""
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    """开始游戏的主循环"""
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # 更新飞船位置
        ship.update()
        
        # 更新子弹位置，删除已经消失的子弹
        gf.update_bullets(bullets)
        
        # 更新屏幕的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
