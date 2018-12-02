#!/usr/bin/env python3

from time import mktime
from random import randint, choice
from datetime import datetime, date, timedelta
from csv import writer, QUOTE_MINIMAL

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

with open('RandomRangeBars.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file, delimiter=',', quotechar='"', quoting=QUOTE_MINIMAL)
    csv_writer.writerow(['date', 'time', 'open', 'high', 'low', 'close'])

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
        date, time = datetime.fromtimestamp(TimeStamp).strftime('%Y-%m-%d/%H:%M:%S').split('/')

        if Randoms['BarType'] == 'Bull':
            Close = Open + (RangeBarHeight - (Randoms['KnotHeight'] / 100 * RangeBarHeight))
            Low = Close - RangeBarHeight
            High = Close
        elif Randoms['BarType'] == 'Bear':
            Close = Open - (RangeBarHeight - (Randoms['KnotHeight'] / 100 * RangeBarHeight))
            High = Close + RangeBarHeight
            Low = Close

        row = [date, time] + ['{:.3f}'.format(i) for i in [Open, High, Low, Close]]
        csv_writer.writerow(row)

