'''Algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento'''

salario = float(input("Qual o salário do funcionário? R$: "))

novoSalario = salario + (salario * 15 / 100)

print(f'O salário do funcionário com o aumento de 15% ficará em {novoSalario:.2f} R$')