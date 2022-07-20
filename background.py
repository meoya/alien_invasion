import pygame

class Background():
    '''设置背景图片'''
    def __init__(self, screen):
        '''初始化背景图片'''
        self.screen = screen
        #加载背景图像并获取其外接矩形
        self.image = pygame.image.load('images/background_001.jpg')

    def blitme(self):
        '''放置背景图片'''
        #设置背景图片的展示尺寸
        image = pygame.transform.scale(self.image, (1200, 800)) 
        #放置背景图片
        self.screen.blit(image, (0, 0))
