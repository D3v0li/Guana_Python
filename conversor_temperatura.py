'''Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF'''

celcius = float(input("Digite a temperatura em graus Celcius: "))
fahreinheit = (1.8 * celcius) + 32

print(f'A temperatura de {celcius}°C corresponde a {fahreinheit:.2f}°F: ')