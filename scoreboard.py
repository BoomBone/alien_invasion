import pygame


class Scoreboard():
    """显示得分信息"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及得属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分图像
        self.prep_score()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
