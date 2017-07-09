#coding=utf-8
class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.rest_stats()
        # 让游戏一开始处于非激活状态
        self.game_active = False

        # 用户等级
        self.level = 1
        # 存储最高分文件名
        self.store_high_score_file_name = 'data/high_score.txt'
        # 获取历史最高分
        try:
            with open(self.store_high_score_file_name) as f_obj:
                self.high_score = int(f_obj.read().strip())
        except FileNotFoundError:
            self.high_score = 0
        
    def rest_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
