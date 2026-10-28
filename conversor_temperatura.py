'''Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF'''

celcius = float(input("Digite a temperatura em graus Celcius: "))
fahreinheit = ((9 * celcius) / 5) + 32

print(f'A temperatura de {celcius}°C corresponde a {fahreinheit:.2f}°F: ')