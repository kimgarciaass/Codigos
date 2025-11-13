horas=int(input("Quanttas horas você trabalhou no mês?:"))
valor=float(input("Qual valor da sua hora?:"))
salario=valor*horas
bonus=salario*0.15
salariototal=bonus+salario
print("Total a receber com bônus:",salariototal)
