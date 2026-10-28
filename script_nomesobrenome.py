'''Script que peça ao usuario seu nome e sobrenome e imprima seu nome completo'''

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_completo = nome + ' ' + sobrenome
print('=' *20)
print(f'''Seu nome completo é:  
{nome_completo}''') 
print('=' *20)