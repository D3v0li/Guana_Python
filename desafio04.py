'''script que pede o ano de nascimento e o ano atual e mostra sua idade'''

nome = input(("Digite seu nome: "))
ano = int(input("Qual o ano de nascimento: ")) 
idade = 2026 - ano

print(f'{nome}, você faz {idade} anos')