def make_snippet(str):
    if len(str) > 5:
        return str[:5] + '...'
    else:
        return str