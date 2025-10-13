nota = float(input("INSIRA A NOTA DO ALUNO: "))
if nota < 0 or nota > 10:
    print("NOTA INVÁLIDO")
else:
    if nota <= 10 and nota >= 9:
        print ("ALUNO CONCEITO A")
    else:
        if nota < 9 and nota >= 7:
            print ("ALUNO CONCEITO B")
        else:
            if nota < 7 and nota >= 5:
                print ("ALUNO CONCEITO C")
            else:
                print ("ALUNO CONCEITO D")