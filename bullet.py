#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
        
        #  加载子弹图像并获取其外接矩形
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        
        #　将子弹初始位置设置在飞船上方
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        
        #self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的位置
        self.rect.y = self.y
        
    
    def draw_bullet(self):
        """在屏幕绘制子弹"""
        #绘制矩形
        #pygame.draw.rect(self.screen, self.color, self.rect)
        #绘制图像
        self.screen.blit(self.image, self.rect)
