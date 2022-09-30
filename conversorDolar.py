print()
print('Programa para calcular real para dólar')
print()

real = float(input('Digite um valor em reais: '))
print()

dolar = float(input('Digite o valor do dólar atual'))
print()

valor_convert = real/dolar
print('R$ {0:.2f} valem: U$ {1:2f}'.format(real, valor_convert)) 