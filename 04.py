minutosTotais = float(input("Informe os minutos: "))

horas = int(minutosTotais // 60)

minutos = int(minutosTotais % 60)

segundos = (minutosTotais % 1) * 60

print(f"Resultado: {horas} h {minutos} min {segundos:.1f} s")