tabuleiro = [["x", "o", "x"],
             ["o", "o", "x"],
             ["o", "x", "o"]]

simbolo_computador = "x"
simbolo_jogador = "o"

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
    if vitoria_linhas(matriz) or vitoria_colunas(matriz) or vitoria_diagonal_principal(matriz) or vitoria_diagonal_secundaria(matriz):
        return True
    else:
        return False

# ------------------------------------------------------------------------


def jogada_do_computador(matriz, simbolopc, simbolojogador):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == "_":
                matriz[i][j] = simbolopc
                if verificacao_vitoria(tabuleiro):
                    return matriz
                else:
                    matriz[i][j] = "_"
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == "_":
                matriz[i][j] = simbolojogador
                if verificacao_vitoria(tabuleiro):
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

