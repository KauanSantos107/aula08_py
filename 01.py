'''Escrever um algoritmo que lê o número de identificação, as 3 notas
obtidas por um aluno nas 3 verificações e a média dos exercícios que
fazem parte da avaliação. Calcular a média de aproveitamento, usando
a fórmula:
MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME ) / 7
A atribuição de conceitos obedece a tabela abaixo:
Média de Aproveitamento Conceito
9,0 A
7,5 e < 9,0 B
6,0 e < 7,5 C
4,0 e < 6,0 D
< 4,0 E
O algoritmo deve escrever o número do aluno, suas notas, a média dos
exercícios, a média de aproveitamento, o conceito correspondente e a
mensagem: APROVADO se o conceito for A,B ou C e REPROVADO se
o conceito for D ou E.'''

aluno = str(input("Nome aluno: "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

mA = (nota1 + (nota2 * 2) + (nota3 * 3) + media  ) / 7

print(f"O aluno {aluno} com as notas {nota1}, {nota2} e {nota3} obeteve média dos exercícios igual à {media} garantiu a média de aproveitamento {mA:.2f}")

if mA == 9:
    print("Aproveitamento A = APROVADO")
elif mA >= 7.5 and mA < 9:
    print("Aproveitamento B = APROVADO")
elif mA >= 6 and mA < 7.5:
    print("Aproveitamento C = APROVADO")
elif mA >= 4 and mA < 6:
    print("Aproveitamento D = REPROVADO")
elif mA < 4:
    print("Aproveitamento E = REPROVADO")