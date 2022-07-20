import sys 
# import pygame 
from random import randint, random

# def run_game(): 
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init() 
#     screen = pygame.display.set_mode((1200, 800)) 
#     background = pygame.image.load("images/abcd.png")
#     pygame.display.set_caption("Alien Invasion") 

#     #设置背景色
#     bg_color = (230, 230, 230)

#     # 开始游戏的主循环 
#     while True: 
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get(): 
#             if event.type == pygame.QUIT: 
#                 sys.exit() 

#         #每次循环时都重绘屏幕
#         screen.blit(background, (0, 0))
#         # screen.fill(bg_color)

#         # 让最近绘制的屏幕可见
#         pygame.display.flip() 

# run_game()

# for a in range(8):
#     # print(a)
#     random_number = randint(0, 7)
#     print(random_number)
alien_image = ['enemyBlue2.png', 'enemyGreen1.png']
print(len(alien_image))
random_number = randint(0, len(alien_image)-1)
print(random_number)
print(alien_image[random_number])
#     print(random_number)

# score = 54
# rounded_score = round(score, -10)
# print(rounded_score)

a = 'abc'
b = 'abc'
c = 'abc'