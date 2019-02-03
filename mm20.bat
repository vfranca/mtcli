@echo off
if %1 == " " (
py sma.py 20 %win%m5.csv
py sma.py 20 %win%m15.csv
py sma.py 20 %win%h1.csv
) else (
py sma.py 20 %1.csv
)
