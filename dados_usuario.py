'''Formulário que pergunte os dados de um usuário'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cpf = int(input("Digite seu CFP: "))
endereco = str(input("Digite seu endereço: "))
bairro = str(input("Digite seu bairro: "))
telefone = input("Digite seu telefone: ")
print("=" *40)
print(f'''Formulário
Nome: {nome}
Idade: {idade}
CPF: {cpf}
Endereço: {endereco}
Bairro: {bairro}
Telefone: {telefone}''')
print("=" *40)