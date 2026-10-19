'''script que pede o ano de nascimento e o ano atual e mostra sua idade'''

nome = input(("Digite seu nome: "))
ano = int(input("Qual o ano de nascimento: ")) 
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano

print(f'{nome}, você vai fazer {idade} anos')