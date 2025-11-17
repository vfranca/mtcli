from mtcli.conf import (
    BEAR,
    BEARBREAKOUT,
    BULL,
    BULLBREAKOUT,
    DOJI,
    DOWNBAR,
    INSIDEBAR,
    OUTSIDEBAR,
    UPBAR,
)


def converte_nome(nome: str):
    if nome.lower() == "up bar":
        return UPBAR
    if nome.lower() == "down bar":
        return DOWNBAR
    if nome.lower() == "inside bar":
        return INSIDEBAR
    if nome.lower() == "outside bar":
        return OUTSIDEBAR
    if nome.lower() == "bull":
        return BULL
    if nome.lower() == "bear":
        return BEAR
    if nome.lower() == "doji":
        return DOJI
    if nome.lower() == "volume ascendente":
        return BULL
    if nome.lower() == "volume descendente":
        return BEAR
    if nome.lower() == "bull breakout":
        return BULLBREAKOUT
    if nome.lower() == "bear breakout":
        return BEARBREAKOUT
    return ""
