#16.	Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a
# seguinte soma:
#S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# O algoritmo deve escrever cada termo gerado e o valor final de S.

n = int(input("Digite um valor inteiro e positivo: "))
if n < 1:
    print ("VALOR INVÁLIDO")
else:
    soma = 0
    for i  in range (1, n+1):
        soma = soma + (1/i)
        print (f"Valores somados = 1/{i} = {1/i:5.2f} ")
    print (f"S = {soma:5.2f}")


