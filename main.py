import pygame
# import pytz

pygame.init()

fo = pygame.font.get_fonts()
print(fo)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

size = [1872,1404]
canvas = pygame.Surface(size)
sysfont = pygame.font.SysFont('notosansmonocjksc', 80)

pygame.display.set_caption("example")

canvas.fill(WHITE)

helloText = sysfont.render(u'HaLakeのイベント情報です', False, BLACK)
canvas.blit(helloText, (0, 0))

CONNPASS_SERIES_ID = 1382 # HaLake
JP_WEEK_DAYS = [u'日', u'月', u'火', u'水', u'木', u'金', u'土']

events = [u'テスト', u'だよ']
cursorStep = 100
currentCursor = cursorStep

for event in events:
    eventText = sysfont.render(event, False, BLACK)
    canvas.blit(eventText, (0, currentCursor))
    currentCursor += cursorStep

pygame.image.save(canvas, 'events.bmp')

