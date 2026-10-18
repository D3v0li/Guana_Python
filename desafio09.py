'''faça um programa que leia um número inteiro e mostre na sua tela a sua tabuada'''

num = int(input("Digite um número para ver sua tabuada: "))
print(f''' 
=== A tabuada do numero {num} é ===''')

for i in range(1,11):
    print(f'{num} x {i} = {num * i}')