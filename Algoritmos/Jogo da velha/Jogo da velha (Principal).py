
#Consigo deixar as linhas do tabuleiro vazias?
#Como sumir com aquela condição do ímpar par

#FUNÇÕES AQUI, CÓDIGO DO JOGO LINHA 135 !!!!

def impar_par(jogador, valor, opcao):
    if opcao == 1:
        opcao = "impar"
    else:
        opcao = "par"
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



def verificacao_empate (matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "_":
                return True
    return False



def verificacao_vitoria(matriz):
    vitoria = False
    def vitoria_linhas(matriz):
        for i in range (len(matriz)):
            if matriz [i] == ["x", "x", "x"] or matriz [i] == ["o", "o", "o"]:
                return True
        return False

    def vitoria_colunas(matriz):
        for i in range (len(matriz)):
            coluna = []
            for j in range (3):
                coluna.append (matriz[j][i])
                if coluna == ["x", "x", "x"] or coluna == ["o", "o", "o"]:
                    return True
        return False

    def vitoria_diagonal_principal(matriz):
        diagonal_principal = []
        for i in range (len(matriz)):
            diagonal_principal.append (matriz[i][i])
            if diagonal_principal == ["x", "x", "x"] or diagonal_principal == ["o", "o", "o"]:
                return True
        return False

    def vitoria_diagonal_secundaria(matriz):
        diagonal_secundaria = []
        for i in range (len(matriz)):
            j = len(matriz) -1 -i
            diagonal_secundaria.append (matriz[i][j])
            if diagonal_secundaria == ["x", "x", "x"] or diagonal_secundaria == ["o", "o", "o"]:
                return True
        return False

    if vitoria_linhas(matriz) or vitoria_colunas(matriz) or vitoria_diagonal_principal(matriz) or vitoria_diagonal_secundaria(matriz):
        return True
    else:
        return False



def jogada_player(matriz, simbolo):
    ok = "nao"
    while ok == "nao":
        linha = int(input("Qual linha deseja jogar? "))
        if linha >= 0 and linha <= 2:
            coluna = int(input("Qual coluna deseja jogar? "))
            if coluna >= 0 and coluna <= 2:
                if matriz[linha][coluna] == "_":
                    matriz[linha][coluna] = simbolo
                    ok = "sim"
                    return matriz
                else:
                    print("Casa já jogada!")
            else:
                print("Coordenada inválida, lembre-se é 0, 1 ou 2")
        else:
            print("Coordenada inválida, lembre-se é 0, 1 ou 2")



def jogada_do_computador(matriz, simbolopc, simbolojogador):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == "_":
                matriz[i][j] = simbolopc
                if verificacao_vitoria(matriz):
                    return matriz
                else:
                    matriz[i][j] = "_"
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == "_":
                matriz[i][j] = simbolojogador
                if verificacao_vitoria(matriz):
                    matriz[i][j] = simbolopc
                    return matriz
                else:
                    matriz[i][j] = "_"
    ok = "nao"
    while ok == "nao":
        import random
        lista = [0, 1, 2]
        i = random.choice(lista)
        j = random.choice(lista)
        if matriz[i][j] == "_":
            matriz[i][j] = simbolopc
            ok = "sim"
            return matriz




#CÓDIGOS DO JOGO


jogador = input("Qual seu nome? ")

jogar_novamente = 1
while jogar_novamente == 1:
    opcao = int(input("Ímpar ou Par? 1- Ímpar   2- Par : "))
    if opcao == 1 or opcao == 2:

        valor = int(input("Jogue seu número: "))

        vencedor, valor, escolhapc = impar_par(jogador, valor, opcao)
        print()
        print()
        print()
        print()
        print()
        print(f"Valor que você jogou: {valor}")
        print(f"Valor jogado pelo computador: {escolhapc}")
        print(f"Vencedor: {vencedor}")

        tabuleiro = [["_", "_", "_"],
                     ["_", "_", "_"],
                     ["_", "_", "_"]]

        if vencedor == jogador:
            simbolo_jogador = "x"
            simbolo_computador = "o"
            while verificacao_vitoria(tabuleiro) == False and verificacao_empate(tabuleiro) == True:
                print()
                for i in range(len(tabuleiro)):
                    print(tabuleiro[i])
                print()
                tabuleiro = jogada_player(tabuleiro, simbolo_jogador)
                ultimo_que_jogou = jogador
                if verificacao_vitoria(tabuleiro) == False and verificacao_empate(tabuleiro) == True:
                    tabuleiro = jogada_do_computador(tabuleiro, simbolo_computador, simbolo_jogador)
                    ultimo_que_jogou = "Computador"

            print()
            for i in range(len(tabuleiro)):
                print(tabuleiro[i])
            print()

            if verificacao_empate(tabuleiro) == False:
                print("Empate HAHAHAHAH!")
                print()
                jogar_novamente = int(input("Jogar novamente? 1-sim 2-não: "))
            else:
                if ultimo_que_jogou == jogador:
                    print("Parabéns, você ganhou!")
                    jogar_novamente = int(input("Jogar novamente? 1-sim 2-não: "))
                else:
                    print("Jesus você é péssimo!")
                    jogar_novamente = int(input("Jogar novamente? 1-sim 2-não: "))



        else:
            simbolo_computador = "x"
            simbolo_jogador = "o"
            while verificacao_vitoria(tabuleiro) == False and verificacao_empate(tabuleiro) == True:
                tabuleiro = jogada_do_computador(tabuleiro, simbolo_computador, simbolo_jogador)
                ultimo_que_jogou = "Computador"
                if verificacao_vitoria(tabuleiro) == False and verificacao_empate(tabuleiro) == True:
                    print()
                    for i in range(len(tabuleiro)):
                        print(tabuleiro[i])
                    print()
                    tabuleiro = jogada_player(tabuleiro, simbolo_jogador)
                    ultimo_que_jogou = jogador
            print()
            for i in range(len(tabuleiro)):
                print(tabuleiro[i])
            print()

            if verificacao_empate(tabuleiro) == False:
                print("Empate HAHAHAHAH!")
                print()
                jogar_novamente = int(input("Jogar novamente? 1-sim 2-não: "))
            else:
                if ultimo_que_jogou == jogador:
                    print("Parabéns, você ganhou!")
                    jogar_novamente = int(input("Jogar novamente? 1-sim 2-não: "))
                else:
                    print("Jesus você é péssimo!")
                    jogar_novamente = int(input("Jogar novamente? 1-sim 2-não: "))
    else:
        print("Valor inválido, achou que ía me pegar né")



