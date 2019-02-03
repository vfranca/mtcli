from trade.expec import get_expec
import sys

taxa_acerto = int(sys.argv[1])
ganho_medio = round(float(sys.argv[2]), 2)
prejuizo_medio = round(float(sys.argv[3]), 2)

e = get_expec(taxa_acerto, ganho_medio, prejuizo_medio)
print("%.1f" % e)
