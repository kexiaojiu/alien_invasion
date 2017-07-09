#coding=utf-8
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, ai_settings, screen, stats):
        """初始化得分属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 显示得分信息时候使用的字体
        self.text_color =(30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)
        
        # 准备初始得分图像和最高分以及用户等级
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
       
        
    def prep_score(self):
        """将得分转化成一幅渲染的图像"""
        # 在大数字中添加逗号作为千位分隔符
        # round(n,k)让小数n精确到小数点后k位，k<0则圆整到-k*10等整数倍
        rounded_score = round(self.stats.score , -1)
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 10
        
        
    def prep_high_score(self):
        """将最高分转化成一幅渲染的图像"""
        # 在大数字中添加逗号作为千位分隔符
        # round(n,k)让小数n精确到小数点后k位，k<0则圆整到-k*10等整数倍
        high_score = round(self.stats.high_score , -1)
        high_score_str = "High Score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
                                                self.text_color,
                                                self.ai_settings.bg_color)
        
        # 将得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top =  self.score_rect.top 
    
        
    def prep_level(self):
        """将用户等级转化成一幅渲染的图像"""
        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
                                                self.text_color,
                                                self.ai_settings.bg_color)
        
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top =  self.score_rect.top + 25
        
    def prep_ships(self):
        """显示还剩余多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 30 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        

        """"显示剩余飞船数目"""
        ship_left_str = str(self.stats.ship_left)
        self.ship_left_image = self.font.render(ship_left_str, True, 
                                                self.text_color,
                                                self.ai_settings.bg_color)
                                                
        # 将剩余飞船数目放在屏幕左上方
        self.ship_left_rect = self.ship_left_image.get_rect()
        self.ship_left_rect.left = self.screen_rect.left + 20
        self.ship_left_rect.top = 30
        
        
        
    def show_score(self):
        # 在屏幕显示得分和最高分、等级
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制剩余飞船
        self.ships.draw(self.screen)
        # 在屏幕显示剩余飞船数目
        self.screen.blit(self.ship_left_image, self.ship_left_rect)
