'''crie um programa que leia quanto dinheiro uma pessoa tem na carteira em real e mostre quantos doláres ela pode comprar'''

real = float(input("Digite quantos reais você tem na carteira: "))

dolares = real / 5.05
print(f'''
Você pode comprar {dolares:.2f} US$''')