from trade.reader import reader
import sys, re

file = "var/"

if len(sys.argv) == 2:
    file += sys.argv[1]
    bars = reader(file)
elif len(sys.argv) == 3:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    if re.match('^[0-9]*$', arg2):
        bars = reader(file, times = int(arg2))
    elif re.match(r'^[0-9]{4}.[0-9]{2}.[0-9]{2}$', arg2):
        bars = reader(file, date = arg2)
elif len(sys.argv) == 4:
    file += sys.argv[1]
    arg3 = int(sys.argv[3])
    arg2 = sys.argv[2]
    bars = reader(file, times = arg3, date = arg2)

for bar in bars:
    print(bar)
