#7.	Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos.
# Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
# 1,2,3,4 = voto para os respectivos candidatos;
# 5 = voto nulo;
# 6 = voto em branco.

voto = int(input("DIGITE O CÓDIGO DO CANDIDATO/VOTO: "))
if voto < 0 or voto > 6:
    print ("CÓDIGO INVALIDO")
else:
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    candidato4 = 0
    nulo = 0
    branco = 0
    while voto != 0:
        if voto == 1:
            candidato1 = candidato1 + 1
        if voto == 2:
            candidato2 = candidato2 + 1
        if voto == 3:
            candidato3 = candidato3 + 1
        if voto == 4:
            candidato4 = candidato4 + 1
        if voto == 5:
            nulo = nulo + 1
        if voto == 6:
            branco = branco + 1
        voto = int(input("DIGITE O CÓDIGO DO CANDIDATO/VOTO: "))
        if voto < 0 or voto > 6:
            print ("CÓDIGO INVALIDO")
print (f"Total de votos Candidato 1: {candidato1}")
print (f"Total de votos Candidato 2: {candidato2}")
print (f"Total de votos Candidato 3: {candidato3}")
print (f"Total de votos Candidato 4: {candidato4}")
print (f"Total de votos Nulos: {nulo}")
print (f"Total de votos Branco: {branco}")
