n1 = float(input("\nDigite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = (n1*2 + n2*3 + n3*5) / (2 + 3 + 5)

if media >= 5:
    situacao = "Aprovado"
elif 3 <= media < 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n--- RESULTADO ---")
print(f"Média final: {media:.2f}")
print(f"Situação do aluno: {situacao}")