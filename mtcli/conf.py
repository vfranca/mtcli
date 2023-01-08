# mtcli
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import os
from dotenv import load_dotenv
import MetaTrader5 as mt5


load_dotenv(".mtcli")

# Dígitos da moeda
digits = os.getenv("DIGITOS")
if digits == None:
    digits = 2
else:
    digits = int(digits)

r = "%." + str(digits) + "f"

# caminho da pasta do MetaTrader 5
mt5.initialize()
info = mt5.terminal_info()
csv_path = os.getenv("MT5_PASTA")
if csv_path == None:
    csv_path = info.data_path + "/MQL5/Files"
mt5.shutdown()
csv_path = csv_path.replace("\\", "/")
csv_path += "/"

# Nome da barra lateral
lateral = os.getenv("LATERAL")
if lateral == None:
    lbl_body_doji = "DOJI"
else:
    lbl_body_doji = lateral

# Nome da barra de alta
alta = os.getenv("ALTA")
if alta == None:
    lbl_body_bull = "VERDE"
else:
    lbl_body_bull = alta

# Nome da barra de baixa
baixa = os.getenv("BAIXA")
if baixa == None:
    lbl_body_bear = "VERMELHO"
else:
    lbl_body_bear = baixa

# nome da sombra superior
lbl_toptail = "TOP"

# nome da sombra inferior
lbl_bottomtail = "BOTTOM"

# Nome da sombra careca
lbl_tail_neutral = "NONE"

# Abreviatura da barra de rompimento de alta
rompimento_alta = os.getenv("ROMPIMENTO_ALTA")
if rompimento_alta == None:
    lbl_buy_pressure = "CP"
else:
    lbl_buy_pressure = rompimento_alta

# Abreviatura da barra de rompimento de baixa
rompimento_baixa = os.getenv("ROMPIMENTO_BAIXA")
if rompimento_baixa == None:
    lbl_sell_pressure = "VD"
else:
    lbl_sell_pressure = rompimento_baixa

# Abreviatura do gap de fechamento
lbl_gap = "G"

# Abreviatura da falha de rompimento
lbl_fbo = ""

# Nome da barra ascendente (up bar)
lbl_asc = "ASC"

# Nome da barra descendente (down bar)
lbl_desc = "DESC"

# Nome da barra externa (outside bar)
lbl_ob = "OB"

# Nome da barra interna (inside bar)
lbl_ib = "IB"

# Percentual do corpo da barra de rompimento
percentual_rompimento = os.getenv("PERCENTUAL_ROMPIMENTO")
if percentual_rompimento == None:
    percentual_rompimento = 50
percentual_rompimento = int(percentual_rompimento)

# Percentual do corpo da barra doji
percentual_doji = os.getenv("PERCENTUAL_DOJI")
if percentual_doji == None:
    percentual_doji = 10
percentual_doji = int(percentual_doji)

# Ativo padrão
SYMBOL = "IBOV"

# Período padrão
PERIOD = "D1"

# Volume padrão
VOLUME = 1

# Stop loss padrão
STOP_LOSS = 250

# Take profit padrão
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
