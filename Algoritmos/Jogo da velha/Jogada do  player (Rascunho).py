tabuleiro = [["j", "o", "x"],
          ["o", "x", "o"],
          ["x", "x", "o"]]

def jogada_player(matriz, simbolo):
    linha = int(input("Qual linha deseja jogar? "))
    coluna = int(input("Qual coluna deseja jogar? "))
    matriz[linha][coluna] = simbolo
    return matriz


# Falta configurar se vai ser jogado "x" ou "o"