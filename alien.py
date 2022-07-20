import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    '''表示单个外星人的类'''
    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置其起始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像，并设置其rect属性
        alien_image_list = ['enemyBlack3.png', 'enemyBlue1.png', 'enemyBlue2.png', 'enemyGreen1.png', 'enemyGreen2.png', 'enemyRed1.png', 'enemyRed2.png', 'character_0008.png', 'character_0001.png', 'character_0003.png']
        random_number = randint(0, len(alien_image_list)-1)
        alien_image = alien_image_list[random_number]
        self.image = pygame.image.load(f'images/{alien_image}')
        self.image = pygame.transform.scale(self.image, (52, 42)) #外星人尺寸
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''向左或向右移动外星人'''
        self.x += (
            self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        )
        self.rect.x = self.x