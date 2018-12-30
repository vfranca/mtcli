import sys

# capital de risco
c = float(sys.argv[1])

# pontos no miniíndice
p = int(sys.argv[2])

# lote para operação
l = c/(p*0.2)
l = int(l)

print("capital de risco: %.2f" % c)
print("pontos no miniíndice: %i" % p)
print("lote para operar: %i" % l)


