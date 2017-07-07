#coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion by Jacob")
    
    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")
    
    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    score = Scoreboard(ai_settings, screen, stats)
    
    # 创建一只飞船、一个子弹编组、一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    """开始游戏的主循环"""
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, score, play_button, ship, 
                        aliens, bullets)
        
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            
            # 更新子弹位置，删除已经消失的子弹
            # 击中外星人时，子弹和飞船一起消失，如果外星人都被消灭，重新创建外星人舰队
            # 每杀一个外星人，加分
            gf.update_bullets(ai_settings, screen, stats, ship, aliens, bullets,
                            score)
            
            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        
        
        # 更新屏幕的图像，并切换到新屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, 
                        play_button, score)

run_game()
