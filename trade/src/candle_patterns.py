
def is_hammer(body, top_shadow, bottom_shadow):
    """Retorna True se o padrão for martelo."""
    if body == 0:
        return False
    if abs(body) <= 25 and top_shadow <=24:
        return True
