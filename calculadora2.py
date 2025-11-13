print("Vamos calcular")# imprime mensagem inicial
calculadora=float(input("Digite um Nº:"))# lê o primeiro número
calculadora2=input("Digite a operação (+ - * /): ") # lê a operação
calculadora3=float(input("Digite o segundo Nº:")) # lê o segundo número
resultado=("+"==calculadora2)*(calculadora+calculadora3)+("-"==calculadora2)*(calculadora-calculadora3)+("*"==calculadora2)*(calculadora*calculadora3)+("/"==calculadora2)*(calculadora/calculadora3)
# soma se operação for +
 # subtração se operação for -
# multiplicação se operação for *
# divisão se operação for /

print("Resultado:",resultado)#mostra resultado
