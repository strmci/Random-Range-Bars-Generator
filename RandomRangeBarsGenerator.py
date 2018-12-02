#!/usr/bin/env python3

from random import randint, choice
from datetime import datetime

#Adjustable parameters
StartingPrice = 10000
StartinTimeStamp = 631180800  # 1. 1. 1990
RangeBarPercent = 3
CandleCount = 10000
MaximumTimeRange = 172800  # 2 days

#Non-adjustable parameters
Open = StartingPrice
Close = 0
High = 0
Low = 0
TimeStamp = StartinTimeStamp
RangeBarHeight = RangeBarPercent / 100 * StartingPrice

for candle_num in range(CandleCount):
    Randoms = {
        'BarType': choice(['Bull', 'Bear']),
        'KnotHeight': randint(0, 100),
        'BarTime': randint(0, MaximumTimeRange),
    }

with open('RandomRangeBars.csv', 'w') as line:
    line.write("date,time,open,high,low,close\n")

    for candle_num in range(CandleCount):

        Randoms = {
            'BarType': choice(['Bull', 'Bear']),
            'KnotHeight': randint(0, 100),
            'BarTime': randint(0, MaximumTimeRange),
        }

        Open = Close
        RangeBarHeight = RangeBarPercent / 100 * Close
        TimeStamp = TimeStamp + Randoms['BarTime']

        if Randoms['BarType'] == 'Bull':
            Close = Open + (RangeBarHeight - (Randoms['KnotHeight'] / 100 * RangeBarHeight))
            Low = Close - RangeBarHeight
            High = Close
        elif Randoms['BarType'] == 'Bear':
            Close = Open - (RangeBarHeight - (Randoms['KnotHeight'] / 100 * RangeBarHeight))
            High = Close + RangeBarHeight
            Low = Close

        time = datetime.fromtimestamp(TimeStamp).strftime('%Y-%m-%d,%H:%M:%S')

        NewBar = '%s,%.3f,%.3f,%.3f,%.3f\n' % (time, Open, High, Low, Close)
        line.write(NewBar)

