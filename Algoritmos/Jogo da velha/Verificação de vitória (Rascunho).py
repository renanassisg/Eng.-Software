tabuleiro = [["o", "o", "x"],
          ["x", "x", "o"],
          ["o", "x", "o"]]

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

print (verificacao_vitoria(tabuleiro))


#Vitoria da diagonal secundaria ok!
#Vitoria da diagonal principal ok!
#Vitoria das linhas ok!
#Vitoria das colunas ok!
