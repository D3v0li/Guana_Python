num_1 = int(input(("Digite um numero: ")))
num_2 = int(input(("Digite outro numero: ")))

soma = num_1 + num_2
subtracao = num_1 - num_2
multiplicacao = num_1 * num_2
divisao = num_1 / num_2
div = num_1 // num_2
raiz = num_1 ** num_2

print(f'''
A soma é {soma},
a subtração é {subtracao},
a multiplicação é {multiplicacao},
a divisão é {divisao:.2f},
o resto da divisão é {div} 
e a exponenciação é {raiz:.2f}''')