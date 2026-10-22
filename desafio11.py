largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura

print(f'A dimensão da sua parede é de: {area}m\u00b2')

tinta = area / 2
print(f'Para pintar essa parede você vai precisar de {tinta}L')