from trade.reader import reader
import sys, re

file = "var/"
p_times = re.compile(r'^[0-9]*$')
p_date = re.compile(r'^[0-9]{4}.[0-9]{2}.[0-9]{2}$')
p_show = re.compile('^[a-z]*$')

# chamada com 1 argumento
if len(sys.argv) == 2:
    file += sys.argv[1]
    bars = reader(file)

# chamada com 2 argumentos
elif len(sys.argv) == 3:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    if p_times.match(arg2):
        bars = reader(file, times = int(arg2))
    elif p_date.match(arg2):
        bars = reader(file, date = arg2)
    elif p_show.match(arg2):
        bars = reader(file, show = arg2)

# chamada com 3 argumentos
elif len(sys.argv) == 4:
    file += sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]
    
    # Quando o 2o argumento é uma data
    if p_date.match(arg2):
        if p_times.match(arg3):
            bars = reader(file, date = arg2, times = int(arg3))
        if p_show.match(arg3):
            bars = reader(file, date = arg2, show = arg3)

    # Quando o 2o argumento é um modo de exibição
    elif p_show.match(arg2):
        if p_times.match(arg3):
            bars = reader(file, show = arg2, times = int(arg3))
        elif p_date.match(arg3):
            bars = reader(file, show = arg2, date = arg3)

for bar in bars:
    print(bar)
