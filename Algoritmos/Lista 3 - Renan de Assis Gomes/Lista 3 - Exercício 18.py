#18.	Escrever um algoritmo que gere e escreva os 3 primeiros números perfeitos. Um número
# perfeito é aquele que é igual a soma dos seus divisores.
i = 0
perf = 0
soma_divisores = -1
while perf != 3:
    if soma_divisores == i:
        perf = perf + 1
        print(f"{perf}° número perfeito: {i}")
    soma_divisores = 0
    i = i + 1
    j = 1
    while j <= (i/2):
        if i % j == 0:
            soma_divisores = soma_divisores + j
        j = j + 1