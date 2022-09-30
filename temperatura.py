temp_c = float(input("Digite a temperatuda em Celsius:"))

temp_f = 1.8*temp_c + 32  #Converte para Fahrenheit 
temp_k = temp_c + 273.15  # converte para Kelvin

print('Temperatuda em Celsius:' + str(temp_c))
print('Temperatura em Fahrenheit: ' + str(temp_f))
print('Temperatura em Kelvin: ' + str(temp_k))