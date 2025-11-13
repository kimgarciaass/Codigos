print("Vamos calcular")#imprime mensagem inicial
calculadora=float(input("Digite um Nº:"))#lê o primeiro número
calculadora3=float(input("Digite o segundo Nº:"))#lê o segundo número
calculadora2=input("Digite a operação (+ - * / % ** √):")#lê a operação
if calculadora2=="+":#soma
    resultado=calculadora+calculadora3
elif calculadora2=="-":#subtração
    resultado=calculadora-calculadora3
elif calculadora2=="*":#multiplicação
    resultado=calculadora*calculadora3
elif calculadora2=="/":#divisão
    resultado=calculadora/calculadora3 if calculadora3!=0 else 0
elif calculadora2=="%":#porcentagem
    resultado=calculadora*calculadora3/100
elif calculadora2=="**":#potência
    resultado=calculadora**calculadora3
elif calculadora2=="√":#raiz quadrada
    resultado=calculadora**0.5 if calculadora>=0 else 0
else:#operação inválida
    resultado=0
print("Resultado:",resultado)#mostra resultado

