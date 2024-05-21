def reverse(s):
    if not isinstance(s, str):
        raise TypeError(f'Expected str, got {type(s)}')
    return s[::-1]