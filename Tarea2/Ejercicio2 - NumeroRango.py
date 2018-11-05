num = int(input("Digite un numero a evaluar: "))
min = int(input("Digite el numero minimo del rango: "))
max = int(input("Digite el numero maximo del rango: "))

def is_in_range(num, min, max):
    esta_en_rango = False
    if num >= min and num <= max:
        esta_en_rango = True
    return esta_en_rango

if is_in_range(num, min, max) == True:
    print("El numero digitado esta en el rango")

else:
    print("El numero digitado no esta en el rango")