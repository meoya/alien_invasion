import pygame

class Settings():
    '''存储所有设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        ## self.background = pygame.image.load("images/background_001.jpg")
        # self.bg_color = (230, 230, 230)
        self.bg_color = (0, 0, 0)

        #飞船的设置
        # self.ship_speed_factor = 1.5 #移动速度
        self.ship_limit = 3 #玩家飞船数量

        #子弹设置
        # self.bullet_speed_factor = 3 #移动速度
        ## self.bullet_width = 3 #子弹宽度
        ## self.bullet_height = 15 #子弹高度
        ## self.bullet_color = (60, 60, 60) #子弹颜色
        ## self.bullet_color = (255, 255, 255) #子弹颜色
        self.bullets_allowed = 999 #屏幕上允许子弹存在的数量

        #外星人设置
        # self.alien_speed_factor = 1 #水平移动速度
        self.fleet_drop_speed = 10 #向下移动速度
        # fleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        #加快游戏节奏的速度
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        #飞船
        self.ship_speed_factor = 1.5 #移动速度

        #子弹
        self.bullet_speed_factor = 3 #移动速度

        #外星人
        self.alien_speed_factor = 1 #水平移动速度

        #fleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        #计分-每个外星人的分值
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置和外星人点数'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

