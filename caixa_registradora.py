valor = float(input("Digite o valor total da compra: R$ "))

if valor <= 100:
    desconto_percentual = 5
elif valor <= 300:
    desconto_percentual = 10
else:
    desconto_percentual = 15

desconto = valor * (desconto_percentual / 100)
valor_final = valor - desconto

print("\n--- RESUMO DA COMPRA ---")
print(f"Valor original: R$ {valor:.2f}")
print(f"Percentual de desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")