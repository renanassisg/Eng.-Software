#8.	Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até n.

variável = int(input("DIGITE A VARIÁVEL: "))
if variável < 1:
    print ("VARIÁVEL INVÁLIDA")
else:
    for i  in range (1, variável+1):
        print (f" {i} x {variável} = {i*variável}")