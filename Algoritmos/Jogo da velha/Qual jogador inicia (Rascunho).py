def impar_par(jogador, valor, opcao):
    import random
    lista = [0, 1, 2, 3, 4, 5]
    escolhaIA = random.choice(lista)
    soma = valor + escolhaIA
    if (soma % 2) == 0:
        resultado = "par"
    else:
        resultado = "impar"
    if opcao == resultado:
        vencedor_par_impar = jogador

    else:
        vencedor_par_impar = "Computador"

    return (vencedor_par_impar, valor, escolhaIA)




jogador = input("Qual seu nome? ")
valor = int(input("Escolha um valor para o par ou ímpar: "))
opcao_par_impar = int(input("Escolha uma opção; 1- Par   2- Ímpar : "))

if opcao_par_impar < 1 or opcao_par_impar > 2:
    print("Valor inválido")
else:
    if opcao_par_impar == 1:
        opcao_par_impar = "par"
    else:
        opcao_par_impar = "impar"

    vencedor, valor, escolhapc = impar_par(jogador, valor, opcao_par_impar)

    print (f"Valor que você escolheu: {valor}")
    print (f"Valor jogado pelo computador: {escolhapc}")
    print (f"Vencedor: {vencedor}")
