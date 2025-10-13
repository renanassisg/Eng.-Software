nota = float(input("INSIRA A NOTA:"))
if nota <0 or nota >100:
    print("NOTA INVÁLIDA")
else:
    if nota >= 60 and nota <= 100:
        print("APROVADO")
    else:
        print("REPROVADO")