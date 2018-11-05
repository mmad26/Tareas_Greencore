num = int(input("Digite el numero a evaluar: "))

def numero_perfecto(num):
    es_perfecto = False
    accum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            accum += divisor

    if accum == num:
        es_perfecto = True

    return es_perfecto


if(numero_perfecto(num) == True):
    print("El numero digitado es un numero perfecto")

else:
    print("El numero digitado no es un numero perfecto")