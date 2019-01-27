from trade.reader import reader
import sys, re

file = "var/"

# 1 argumento
if len(sys.argv) == 2:
    file += sys.argv[1]
    bars = reader(file)
# 2 argumentos
elif len(sys.argv) == 3:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    if re.match('^[0-9]*$', arg2):
        bars = reader(file, times = int(arg2))
    elif re.match(r'^[0-9]{4}.[0-9]{2}.[0-9]{2}$', arg2):
        bars = reader(file, date = arg2)
    elif re.match(r'^[a-z]*$', arg2):
        bars = reader(file, show = arg2)

# 3 argumentos
elif len(sys.argv) == 4:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = int(sys.argv[3])
    
    if re.match('^[0-9]{4}.[0-9]{2}.[0-9]{2}$', arg2):
        bars = reader(file, date = arg2, times = arg3)
    elif re.match('^[a-z]*$', arg2):
        bars = reader(file, show = arg2, times = arg3)

for bar in bars:
    print(bar)
