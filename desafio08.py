'''escreva um programa que leia um valor em metros e exiba-o covertido em centimetros e milimetros'''

numero_Metro = float(input("Digite um número em metros: "))

centimetros = numero_Metro * 100
milimetros = numero_Metro * 1000

print(f'''
O número convertido em centimetros é {centimetros:.2f}
e o numero convertido em milimetros é igual a {milimetros:.2f}
''') 