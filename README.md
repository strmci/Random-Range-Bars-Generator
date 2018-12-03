# Range-Bars-Generator
Dynamic Random Range Bars Generator

This python code generates dynamic random range bars, it can be used in Multicharts platform to backtest automated strategies on random data. Every new range bar has different height according to last close and RangeBarPercent.

#Adjustable parameters

StartingPrice = 10000 # Starting price for the chart

StartingTimeStamp = 631180800   #Starting date and time for the chart (1. 1. 1990)

RangeBarPercent = 3 # Range Bar height

CandleCount = 10000 # Candles to create

MaximumTimeRange = 172800  #  Maximum time of one bar (2 days)
