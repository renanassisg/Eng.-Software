#14.	Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o
# código e o preço de custo de cada produto e calcule o preço novo. Calcule também, a média
# dos preços com e sem aumento. Mostre o código e o preço novo de cada produto e, no final, as médias.
# A entrada de dados deve terminar quando for lido um código de produto negativo.

codigo = int(input("Digite o código do produto: "))
somapreços = 0
quantidade = 0
if codigo < 0:
    print ("Código inválido")
else:
    while codigo >= 0:
        quantidade = quantidade + 1
        valor = float(input("Digite o preço de custo do produto acima: "))
        somapreços = somapreços + valor
        print (f"Produto {codigo}, valor reajustado para: {valor * 1.2:5.2f} R$")
        codigo = int(input("Digite o código do produto: "))
    mediapreços = somapreços / quantidade
    print (f" Média dos preços anterior: {mediapreços} R$")
    print (f" Média dos preços com reajuste: {mediapreços*1.2:5.2f} R$ ")

