num1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
num2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
num3 = float(input("DIGITE O TERCEIRO NÚMERO: "))
num4 = float(input("DIGITE O QUARTO NÚMERO: "))
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
if num4 < menor:
    menor = num4
print ("MENOR NÚMERO É: ",menor)
