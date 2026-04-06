'''Crie um algoritmo que leia quatro valores digitados pelo usuário: n, a, b, c.
a) Se n = 1 imprimir os três valores a, b, c em ordem crescente.
b) Se n = 2 escrever os três valores a, b, c em ordem decrescente.
c) Se n = 3 escrever os três valores a, b, c de forma que o maior fique no
meio'''

n = int(input("Valor n ( 1, 2 ou 3) "))
a = float(input("Valor A: "))
b = float(input("Valor B: "))
c = float(input("Valor C: "))

valores = [a, b, c]

if n == 1:
    valores.sort()
    print(f"Ordem crescente: {valores}")

elif n == 2:
    valores.sort(reverse=True)
    print(f"Ordem decrescente: {valores}")

elif n == 3:
    valores[1], valores[2] = valores[2], valores[1]
    print(f"Maior no meio: {valores}")

