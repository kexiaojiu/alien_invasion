#coding=utf-8
class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.rest_stats()
        # 让游戏一开始处于非激活状态
        self.game_active = False
        # 任何情况都不应该重置最高分
        self.high_score = 0
        
        
    def rest_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
