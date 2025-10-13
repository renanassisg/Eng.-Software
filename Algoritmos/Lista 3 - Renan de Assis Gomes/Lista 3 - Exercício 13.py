#13.	Faça um algoritmo que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
# números lidos. O número que encerrará a leitura será zero.
num = int(input("Digite um valor positivo, para encerrar digite 0: "))
if num == 0:
    print("Encerrado")
else:
    pares = 0
    impares = 0
    somapares = 0
    somatotal = 0
    mediapares = 0
    while num != 0:
        if num < 0:
            print("Valor inválido")
        else:
            somatotal = somatotal + num
            if num % 2 == 0:
                pares = pares + 1
                somapares = somapares + num
            else:
                impares = impares + 1
        num = int(input("Digite um valor positivo, para encerrar digite 0: "))
    mediatotal = somatotal / (pares+impares)
    if pares > 0:
        mediapares = somapares / pares
    print ("Encerrado: ")
    print (f"Pares : {pares}")
    print (f"Ímpares : {impares}")
    print (f"Média dos valores pares : {mediapares:5.2f}")
    print (f"Média total dos valores lidos : {mediatotal:5.2f}")


