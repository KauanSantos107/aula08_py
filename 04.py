'''Escreva um programa que converta um intervalo de tempo dado em minutos,
em horas, minutos e segundos. Por exemplo, se o tempo dado for 145,87
minutos, o programa deve fornecer 2 h 25 min 52,2 s.'''

minutosTotais = float(input("Informe os minutos: "))

horas = int(minutosTotais // 60)

minutos = int(minutosTotais % 60)

segundos = (minutosTotais % 1) * 60

print(f"Resultado: {horas} h {minutos} min {segundos:.1f} s")
