# coding=utf-8
import json
import pygame,os



import random_truple

class Settings:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        # coding=utf-8
        self.bg_color = (random_truple.rn(3))
        self.screen_size = (1200,800)

        self.ship_speed = 1.5
        self.ship_num = 5
        self.ship_limit = 5

        self.bullet_speed = 0.8
        self.bullet_color = (20,20,200)

        self.enemy_speedx = 0.1
        self.enemy_speedy = 0.08
        self.enemy_width = 41
        self.speedup = 1.05
        # coding=utf-8
        self.score = "0"
        self.bullet_sound = pygame.mixer.Sound(os.path.join("sound\子弹发射.wav.wav"))
        self.collision_sound = pygame.mixer.Sound(os.path.join("sound\爆炸音效.wav"))

        # self.high_score = str(dict_score["得分"])
        self.high_score = "0"




    def increse_speed(self):
        """提高速度"""

        self.enemy_speedy *= self.speedup*0.95
        self.enemy_speedx *= self.speedup*0.96
        self.bullet_speed *= self.speedup*0.95

    def initialize(self):
        """初始化速度"""
        self.enemy_speedx = 0.1
        self.enemy_speedy = 0.08
        self.bullet_speed = 0.5
        self.score = "0"




