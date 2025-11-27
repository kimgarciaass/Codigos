temperaturas = []

print("\nDigite as temperaturas dos 30 dias:")

for i in range(30):
    temp = float(input(f"Dia {i+1}: "))
    temperaturas.append(temp)

media_mes = sum(temperaturas) / 30
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)

dias_acima_273 = sum(1 for t in temperaturas if t > 27.3)

print("\n--- RELATÓRIO DO MÊS ---")
print(f"Temperatura média do mês: {media_mes:.2f}°C")
print(f"Maior temperatura: {maior_temp:.2f}°C")
print(f"Menor temperatura: {menor_temp:.2f}°C")
print(f"Dias acima de 27.3°C: {dias_acima_273}")
