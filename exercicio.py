nota1 = int(input("insira a primeira nota:"))

nota2 = float(input("insira a segunda nota:"))

nota3 = float(input("insira a terceira nota:"))

nota4 = int(input("insira a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print("aprovado")
else:
    print("reprovado")
