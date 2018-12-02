#!/usr/bin/env python3

import random
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

#clear file
f = open("RandomRangeBars.csv", "w")
f.truncate()
f.close()

for i in range(1, CandleCount):

    #Randoms (Bull, Bear, Knot, BarTime)
    BarType = random.randrange(1, 3, 1)
    KnotHeight = random.randrange(1, 101, 1)
    BarTime = random.randrange(1, MaximumTimeRange, 1)

    if i == 1:
        Open = StartingPrice
        TimeStamp = StartinTimeStamp
        with open('RandomRangeBars.csv', 'a') as line:
            line.write("date,time,open,high,low,close")
            line.write("\n")
    else:
        Open = Close
        RangeBarHeight = RangeBarPercent / 100 * Close
        TimeStamp = TimeStamp + BarTime

    #BullBar
    if BarType == 1:
        Close = Open + (RangeBarHeight - (KnotHeight / 100 * RangeBarHeight))
        Low = Close - RangeBarHeight
        High = Close
    #BearBar
    elif BarType == 2:
        Close = Open - (RangeBarHeight - (KnotHeight / 100 * RangeBarHeight))
        High = Close + RangeBarHeight
        Low = Close

    time = datetime.datetime.fromtimestamp(TimeStamp).strftime('%Y-%m-%d,%H:%M:%S')

    NewBar = (str(time)+','+str(format(Open, '.3f'))+','+str(format(High, '.3f'))+','+str(format(Low, '.3f'))+','+str(format(Close, '.3f')))


    with open('RandomRangeBars.csv', 'a') as line:
        line.write(NewBar)
        line.write("\n")



