def on_alkuluku(numero):
    if numero < 2:
        return False
    for n in range(2, int(numero/2)+1):
        if numero % n == 0:
            return False
    else:
        return True

