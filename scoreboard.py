import pygame
class Scoreboard:
    def __init__(self, settings, screen):
        pygame.init()
        self.settings = settings
        self.screen = screen

        # 计分板的尺寸和颜色
        self.width, self.height = 150, 30
        self.score_color = (250, 0, 0)
        self.board_color = (100, 20, 250)
        #得分文字颜色和尺寸
        self.text_color = (0,0,250)
        self.font = pygame.font.SysFont(None, 45)

        # 创建计分板的rect对象，并放在右上角
        screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = screen_rect.right
        self.rect.top = 15
        #创建最高得分计分板的rect对象，并放置于midtop
        screen_rect = self.screen.get_rect()
        self.high_rect = pygame.Rect(0, 0, self.width, self.height)
        self.high_rect.midtop = screen_rect.midtop
      
        
        #创建得分数字的rect对象
        self.msg_image = self.font.render(settings.score, True, self.score_color,self.board_color)
        self.msg_rect = self.msg_image.get_rect()
        #创建最高得分的rect对象
        self.high_msg_image = self.font.render(settings.high_score, True, self.score_color, self.board_color)
        self.high_msg_rect = self.high_msg_image.get_rect()
        



  
    def draw_score(self,settings):
        """绘制分数和文字"""
        # 得分数字的位置
        self.msg_image = self.font.render(settings.score, True, self.score_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.right = self.rect.right
        self.msg_rect.top = 20
        # 最高得分数字的位置
        self.high_msg_image = self.font.render(settings.high_score, True, self.score_color)
        self.high_msg_rect = self.high_msg_image.get_rect()
        self.high_msg_rect.right = self.high_rect.right


        # 文字的位置
        self.text_image = self.font.render("score:",True,self.text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.left = self.rect.left
        self.text_rect.top = 20
        #最高文字的位置
        self.high_text_image = self.font.render("highest score:", True, self.text_color)
        self.high_text_rect = self.high_text_image.get_rect()
        self.high_text_rect.left = self.high_rect.left-120

        
        
        # 绘制计分板
        # self.screen.fill(self.board_color, self.rect)
        # self.screen.fill(self.board_color, self.high_rect)

        # 显示文字
        self.screen.blit(self.high_msg_image,self.high_msg_rect)
        self.screen.blit(self.msg_image, self.msg_rect)
        # 显示数字

        self.screen.blit(self.text_image,self.text_rect)
        self.screen.blit(self.high_text_image, self.high_text_rect)

      

