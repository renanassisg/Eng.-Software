nome = input("DIGITE O NOME DO ALUNO: ")
prova1 = float(input("DIGITE SUA NOTA DA 1º PROVA: "))
prova2 = float(input("DIGITE SUA NOTA DA 2º PROVA: "))
trabalho = float(input("DIGITE SUA NOTA DO TRABALHO: "))
faltas = int(input("QUANTAS FALTAS ELE TEVE: "))
notafinal = (3*prova1+5*prova2+2*trabalho)/10
if faltas > 15:
    print("ALUNO REPROVADO")
else:
    if notafinal >= 6:
        print("ALUNO APROVADO, MÉDIA:", notafinal)
    else:
        print("MÉDIA",notafinal,"ALUNO PRECISARÁ FAZER A PROVA FINAL")