from datetime import datetime

datahora = "2025.03.01 07:33:00"
datahora = datetime.strptime(datahora, "%Y.%m.%d %H:%M:%S")
print(datahora)
data = datahora.date()
print(data)
hora = datahora.time()
print(hora)

if "2025-03-01" == str(data):
    print("comparacao ok")
else:
    print("comparacao errada")
