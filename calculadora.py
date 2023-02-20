import math

raiz = bool(input("Voce Quer Fazer Raiz3?:"))
    

numero3 = int(input("Digite Sua Raiz:"))

if raiz == True:
    print(math.sqrt(numero3))


numero = int(input("Digite O 1 numero:"))

numero2 = int(input("Digite O 2 numero:"))



tipodeconta = str(input("Tipo de Calculo:"))

if tipodeconta == "+":
    print(numero+numero2)

if tipodeconta == "-":
    print(numero-numero2)


if tipodeconta == "*":
    print(numero*numero2)

if tipodeconta == "/":
    print(numero/numero2)

if tipodeconta =="**":
    print(math.pow(numero, numero2))





##�Quitto