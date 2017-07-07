#coding=utf-8
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 置背景颜色
        self.bg_color = (230, 230, 230)
        
        # 飞船速度设置
        self.ship_limit = 3
        
        # 子弹设置
        self.bullet_color = (60, 60, 60)
        # 限制未消失的子弹数目
        self.bullets_allowed = 9
        
        # 外星人速度设置
        self.fleet_drop_speed = 10
        
        # 以什么样的速度加快游戏的节奏
        self.speedup_scale = 1.2
        
        # 外星人点数提高的速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        #fleet_derection为1表示右移，-1表示左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50
    
    
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale   
        
        self.alien_points = int(self.alien_points * self.score_scale)  
