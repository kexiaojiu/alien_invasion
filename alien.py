#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其初始位置"""
        super().__init__()

        
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像并获取其外接矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 将外星人放在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
    
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
        
        
    #def update(self):
        """调整外星人位置"""
            
