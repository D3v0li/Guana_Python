''' faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto'''

precoProduto = float(input("Digite o preço do produto em R$: "))

novoPreco = precoProduto - (precoProduto * 5 / 100)

print(f'O produto que custava {precoProduto} com 5% de desconto passa a custar: {novoPreco:.2f}')