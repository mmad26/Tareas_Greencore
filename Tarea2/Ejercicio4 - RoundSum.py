def num_round(num1, base = 10):
    return base * (round(float(num1) / base))

def sum_round(num1, num2, num3):
    return num_round(num1) + num_round(num2) + num_round(num3)

primernumero = int(input("Digite el primer numero: "))
segnumero = int(input("Digite el segundo numero: "))
tercernumero = int(input("Digite el tercer numero: "))

print(sum_round(primernumero, segnumero, tercernumero), "es la suma de los numeros redondeados.")

