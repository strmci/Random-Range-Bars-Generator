#!/usr/bin/env python3

from random import randint, choice
import datetime

#Adjustable parameters
StartingPrice = 10000
StartinTimeStamp = 631180800  # 1. 1. 1990
RangeBarPercent = 3
CandleCount = 10000
MaximumTimeRange = 172800  # 2 days

#Non-adjustable parameters
Close = 0
High = 0
Low = 0
TimeStamp = 0
RangeBarHeight = RangeBarPercent / 100 * StartingPrice

for candle_num in range(CandleCount):
    Randoms = {
        'BarType': choice(['Bull', 'Bear']),
        'KnotHeight': randint(0, 100),
        'BarTime': randint(0, MaximumTimeRange),
    }

    if candle_num == 0:
        Open = StartingPrice
        TimeStamp = StartinTimeStamp
        with open('RandomRangeBars.csv', 'a') as line:
            line.write("date,time,open,high,low,close\n")
    else:
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

    time = datetime.datetime.fromtimestamp(TimeStamp).strftime('%Y-%m-%d,%H:%M:%S')

    with open('RandomRangeBars.csv', 'a') as line:
        NewBar = '%s,%.3f,%.3f,%.3f,%.3f\n' % (time, Open, High, Low, Close)
        line.write(NewBar)

