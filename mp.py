import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = float(sys.argv[4])

range = abs(a - b)
alvo1 = c + range
alvo2 = d - range

res = "%2.f %2.f" % (alvo1, alvo2)
print(res)
