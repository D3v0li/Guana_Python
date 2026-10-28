'''Script que pergunte ao usuario quanto ele ganha por hora e quantas horas ele trabalhou no mês e imprima o salario total'''

valor_hora = float(input("Digite o valor da hora trabalhada: "))
hora_trabalhada = float(input("Digite as horas trabalhadas: "))

salario_total = valor_hora * hora_trabalhada
print(f'O funcionario recebe o total de {salario_total} R$')