uno = int(input("Digite un numero: "))
dos = int(input("Digite otro numero: "))
tres = int(input("Digite un ultimo numero: "))


def numero_mas_alto(uno, dos, tres):
    mayor = 0
    if uno > dos and uno > tres:
        mayor = uno
    elif dos > uno and dos > tres:
        mayor = dos
    else:
        mayor = tres
    return mayor

print(numero_mas_alto(uno, dos, tres), "es el numero mas alto de los tres.")