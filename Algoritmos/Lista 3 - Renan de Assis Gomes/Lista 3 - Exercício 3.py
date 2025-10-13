#3.	Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial
# de N (N!).

n = int(input("DIGITE O VALOR DE N: "))
if n <= 0:
    print ("Valor inválido!")
else:
    fatorial = 1
    for i in range (1, n+1):
        fatorial = fatorial*i
    print (f"Fatorial de {n} = {fatorial}")