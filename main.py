# -*- coding: utf-8 -*-
import pygame
import connpass_event_filter as cef
from datetime import datetime
import pytz
from dateutil import parser

pygame.init()

fo = pygame.font.get_fonts()
print(fo)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

size = [1872,1404]
canvas = pygame.Surface(size)
fontM = pygame.font.SysFont('notosansmonocjksc', 80)
fontL = pygame.font.SysFont('notosansmonocjksc', 120, bold=True)

canvas.fill(WHITE)

helloText = fontM.render(u'HaLakeイベント情報', False, BLACK)
canvas.blit(helloText, (0, 0))

CONNPASS_SERIES_ID = 1382 # HaLake
JP_WEEK_DAYS = [u'日', u'月', u'火', u'水', u'木', u'金', u'土']

yStepSection = 50
yStepFontM = 100
yStepFontL = 150
currentCursor = yStepFontM + yStepSection

events = cef.get_events(CONNPASS_SERIES_ID)
events = cef.remove_past_events(events)
events = cef.sort_by_started_at(events)

def get_datetime_str(target_datetime):
    date_str = target_datetime.strftime('%m/%d')
    week_day_str = JP_WEEK_DAYS[int(target_datetime.strftime('%w'))]
    week_day_str = '(' + week_day_str + ')'
    time_str = target_datetime.strftime('%H:%M')
    return date_str + week_day_str + time_str

for event in events:
    titleBlock = fontL.render(event['title'], False, BLACK)
    canvas.blit(titleBlock, (0, currentCursor))
    currentCursor += yStepFontL

    started_at = parser.parse(event['started_at'])
    started_at_str = get_datetime_str(started_at)
    accepted_str = ''
    if 'accepted' in event and event['accepted'] != 0:
        accepted_str = '  ' + str(event['accepted']) + u'人参加予定'
    infoText = started_at_str + accepted_str
    infoBlock = fontM.render(infoText, False, BLACK)
    canvas.blit(infoBlock, (0, currentCursor))
    currentCursor += yStepFontM + yStepSection

jpNow = datetime.now(pytz.timezone('Asia/Tokyo'))
currentTimeStr = get_datetime_str(jpNow)
updatedTimeText = fontM.render(currentTimeStr + u'更新', False, BLACK)
canvas.blit(updatedTimeText, (0, currentCursor))

canvas = pygame.transform.rotate(canvas, 180)
pygame.image.save(canvas, 'events.bmp')

