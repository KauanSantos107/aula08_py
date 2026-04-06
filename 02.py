'''Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:
"São múltiplos" ou "Não são múltiplos"'''

valorA = int(input("Valor A: "))
valorB = int(input("Valor B: "))

if valorA == 0 or valorB == 0:
    print("Zero não entra para este caso")

elif valorA % valorB == 0 or valorB % valorA == 0:
    print("São múltiplos")
    
else:
    print("Não são múltiplos")