# -*- coding: utf-8 -*-
import sys


# bankrooll capital de trade
br=353.00

ta=int(sys.argv[1])/100
po=float(sys.argv[2])

# k = coeficiente de kelly
k = ta - (1 - ta) / po

# capital arriscado por trade
c = br * k

print("Taxa de Acerto: %.2f" % ta)
print("Payoff: %.1f" % po)
print("Taxa de risco por trade: %.2f" % k)
print("Capital por trade: %.2f" % c)

