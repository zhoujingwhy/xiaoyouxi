class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=False
        # 在任何情况下都不应该重置最高分
        self.high_score=0

    def reset_stats(self):
        self.ship_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
