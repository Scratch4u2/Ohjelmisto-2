def on_alkuluku(numero):
    if numero < 2:
        return False
    for n in range(2, int(numero/2)+1):
        if numero % n == 0:
            return False
    else:
        return True

u_input = int(input("Anna numero: \n"))

if on_alkuluku(u_input):
    print(f"{u_input} on alkuluku")
else:
    print(f"{u_input} ei ole alkuluku")