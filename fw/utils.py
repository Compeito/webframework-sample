def flatten(x):
    """
    https://qiita.com/hoto17296/items/e1f80fef8536a0e5e7db
    """
    return [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]
