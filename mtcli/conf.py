# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()
digits = int(os.getenv("DIGITS"))
r = "%." + str(digits) + "f"
csv_path = os.getenv("CSV_PATH")

lbl_body_doji = "DOJI"
lbl_body_bull = "VERDE"
lbl_body_bear = "VERMELHO"
lbl_toptail = "TOP"
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

ORDER_REFUSED = "Ordem recusada! Verifique a conexão com o MetaTrader"
CONNECTION_MISSING = "Falha na conexao com o MetaTrader"
PRICE_CURRENT_ERROR = (
    "O preço atual não foi encontrado! Verifique a conexão com o MetaTrader"
)
POSITION_MODIFIED_SUCCESS = "A posição foi alterada com sucesso!"
POSITION_MODIFIED_ERROR = "Ocorreu um erro! Verifique a conexão com o MetaTrader"
