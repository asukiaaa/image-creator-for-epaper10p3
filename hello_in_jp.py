# -*- coding: utf-8 -*-
import pygame

pygame.init()

# fo = pygame.font.get_fonts()
# print(fo)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

size = [1872,1404]
surface = pygame.Surface(size)
sysfont80 = pygame.font.SysFont('notosansmonocjksc', 80)
sysfont200 = pygame.font.SysFont('notosansmonocjksc', 200)

surface.fill(WHITE)

helloText = sysfont200.render(u'こんにちは。', False, BLACK)
surface.blit(helloText, (0, 0))

infoText = sysfont80.render(u'ePaperに出力しています。', False, BLACK)
surface.blit(infoText, (0, 270))

pygame.image.save(surface, 'hello_in_jp.bmp')
