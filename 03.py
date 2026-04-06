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

