import sys,tkinter.messagebox as mgb
import tkinter
root = tkinter.Tk()
root.withdraw()

import pygame,time
class GameStats:
    def __init__(self,settings):
        self.settings = settings
        self.game_active = False
        # 创建实例时，初始化飞机数量。


    def reset_stats(self,ship,enemies,settings):
        """c初始化必要信息"""
        if self.settings.ship_num <= 0:
            self.game_active = False

            if mgb.askyesno("提示","游戏结束了，你还要玩吗？"):
                self.game_active = True
                settings.initialize()
                self.settings.ship_num = self.settings.ship_limit
                print("飞船用完了，已经补充了新的飞船")
            else:
                sys.exit()






