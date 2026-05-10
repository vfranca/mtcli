def body_size(bar):
    return abs(bar.close - bar.open)


def is_inside_bar(prev, curr):
    return curr.high <= prev.high and curr.low >= prev.low
