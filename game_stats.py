#coding=utf-8
class GameStats():
    """跟踪邮箱的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.game_active = True
        self.rest_stats()
        
    def rest_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ship_left = self.ai_settings.ship_limit
