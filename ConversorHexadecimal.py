mensagem = 'Valor decimal: {0}\nValor Hexadecimal: {1}'

print('Programa para conventer de decimal para hexa')
print()

num_dec = int(input('Digite um número: '))
print()

num_hex = format(num_dec, 'X')
print()

print(mensagem.format(num_dec, num_hex))