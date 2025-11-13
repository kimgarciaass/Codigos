import random

palavras = ["python", "banana", "futebol", "computador", "escola"]
palavra = random.choice(palavras)
acertos = "_" * len(palavra)
tentativas = 6

while tentativas > 0 and "_" in acertos:
  print(acertos)
  l = input("Letra: ")
  if l in palavra:
    novo = ""
    for i in range(len(palavra)):
      novo += l if palavra[i] == l else acertos[i]
    acertos = novo
  else:
    tentativas -= 1
    print("Errou! Restam", tentativas)

print("Ganhou!" if "_" not in acertos else "Perdeu! Palavra: " + palavra)
