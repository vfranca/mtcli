import sys

if len(sys.argv) > 1:
    prices = []
    sys.argv.pop(0)
    for price in sys.argv:
        prices.append(float(price))
    medio = round(sum(prices) / len(prices), 1)
    print(medio)
else:
    print("Informe os preços")
    