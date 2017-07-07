#coding=utf-8
import pygame.font

class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, ai_settings, screen, stats):
        """初始化得分属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # 显示得分细腻些时候使用的字体
        self.text_color =(30, 30, 30)
        self.font = pygame.font.SysFont(None, 20)
        
        # 准备初始得分图像和最高分
        self.prep_score()
        self.prep_high_score()
       
        
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
        
    def show_score(self):
        # 在屏幕显示得分和最高分
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
