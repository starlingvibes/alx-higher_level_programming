def islower(c):
    asciicode = ord(c)
    if asciicode >= 97 and asciicode <= 122:
        return True
    elif asciicode >= 65 and asciicode <= 90:
        return False
