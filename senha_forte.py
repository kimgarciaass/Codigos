senha = input("\nDigite uma senha: ")

erros = []

if len(senha) < 8:
    erros.append("A senha deve ter pelo menos 8 caracteres.")

if not any(c.isupper() for c in senha):
    erros.append("A senha deve ter pelo menos 1 letra maiúscula.")

if not any(c.islower() for c in senha):
    erros.append("A senha deve ter pelo menos 1 letra minúscula.")

if not any(c.isdigit() for c in senha):
    erros.append("A senha deve ter pelo menos 1 número.")

caracteres_especiais = "!@#$%^&*()-_=+[]{};:<>/?|\\"
if not any(c in caracteres_especiais for c in senha):
    erros.append("A senha deve ter pelo menos 1 caractere especial.")

print("\n--- VERIFICAÇÃO DA SENHA ---")
if len(erros) == 0:
    print("Senha forte!")
else:
    print("Senha fraca!")
    print("Regras não atendidas:")
    for erro in erros:
        print(" -", erro)
        