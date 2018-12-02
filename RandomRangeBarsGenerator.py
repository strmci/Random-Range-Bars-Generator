#!/usr/bin/env python3

from time import mktime
from random import randint, choice
from datetime import datetime, date, timedelta

#Adjustable parameters
StartingPrice = 10000
StartingTimeStamp = mktime(date(1990, 1, 1).timetuple())
RangeBarPercent = 3
CandleCount = 10000
MaximumTimeRange = timedelta(days=2).total_seconds()

#Non-adjustable parameters
Open = StartingPrice
Close = 0
High = 0
Low = 0
TimeStamp = StartingTimeStamp
RangeBarHeight = RangeBarPercent / 100 * StartingPrice

with open('RandomRangeBars.csv', 'w') as line:
    line.write("date,time,open,high,low,close\n")

    for i, candle_num in enumerate(range(CandleCount)):
        Randoms = {
            'BarType': choice(['Bull', 'Bear']),
            'KnotHeight': randint(1, 100),
            'BarTime': randint(1, MaximumTimeRange),
        }

        if i != 0:
            Open = Close
            RangeBarHeight = RangeBarPercent / 100 * Close
            TimeStamp += Randoms['BarTime']

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

