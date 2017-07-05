#coding=utf-8
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 置背景颜色
        self.bg_color = (230, 230, 230)
        
        # 飞船速度设置
        self.ship_speed_factor = 1.5
        
        # 子弹设置
        self.bullet_speed_factor = 5
        #self.bullet_width = 3
        #self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 限制未消失的子弹数目
        self.bullets_allowed = 9
        
        # 外星人速度设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_derection为1表示右移，-1表示左移
        self.fleet_direction = 1
