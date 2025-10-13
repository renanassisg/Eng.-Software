#10.	Escrever um algoritmo que leia um número n que indica quantos valores devem ser
# lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial deste valor.

num = int(input("QUANTO VALORES SERÃO DIGITADOS? "))
if num < 1:
    print ("NÚMERO INVÁLIDO")
else:
    for i in range (num):
        valor = int(input("DIGITE UM VALOR: "))
        fatorial = 1
        for j in range (1, valor+1):
            fatorial = j*fatorial
        print (f"FATORIAL DE {valor} É {fatorial}")