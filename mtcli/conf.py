"""
mtcli
Variáveis de configuração
"""
import os
from dotenv import load_dotenv
import MetaTrader5 as mt5


load_dotenv()

# Dígitos da moeda
digits = os.getenv("DIGITS")
if digits == None: digits = 2
else: digits = int(digits)

r = "%." + str(digits) + "f"

# caminho dos dados do MetaTrader 5
mt5.initialize()
info = mt5.terminal_info()
csv_path = os.getenv("CSV_PATH")
if csv_path == None: csv_path = info.data_path + "/MQL5/Files"
mt5.shutdown()
csv_path = csv_path.replace("\\", "/")
csv_path += "/"

# Nome do corpo doji
corpo_doji = os.getenv("CORPO_DOJI")
if corpo_doji == None: lbl_body_doji = "DOJI"
else: lbl_body_doji = corpo_doji

# Nome do corpo de alta
alta=os.getenv("CORPO_DE_ALTA")
if alta == None: lbl_body_bull = "VERDE"
else: lbl_body_bull = alta

# Nome do corpo de baixa
baixa = os.getenv("CORPO_DE_BAIXA")
if baixa == None: lbl_body_bear = "VERMELHO"
else: lbl_body_bear = baixa

# nome da sombra superior
lbl_toptail = "TOP"

# nome da sombra inferior
lbl_bottomtail = "BOTTOM"

lbl_tail_neutral = "NONE"
lbl_buy_pressure = "CP"
lbl_sell_pressure = "VD"

lbl_gap = "G"
lbl_fbo = ""

lbl_asc = "ASC"
lbl_desc = "DESC"
lbl_ob = "OB"
lbl_ib = "IB"

SYMBOL = "WINV19"
PERIOD = "H1"
VOLUME = 1
STOP_LOSS = 250
TAKE_PROFIT = 500

ORDER_ERROR = "Órdem recusada"
PRICE_CURRENT_ERROR = "Preço indisponível"
POSITION_MODIFIED_SUCCESS = "Posição alterada"
POSITION_MODIFIED_ERROR = "Alteração recusada"
CONNECTION_ERROR = "MetaTrader desconectado"
ORDER_CANCELED_SUCCESS = "Todas as órdens foram canceladas"
ORDER_CANCELED_ERROR = "Cancelamento Recusado"
POSITION_CANCELED_SUCCESS = "Todas as posições foram canceladas"
POSITION_CANCELED_ERROR = "Cancelamento Recusado"
