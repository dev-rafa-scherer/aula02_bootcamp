import math
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# numero01 = int(input("Digite o primeiro numero: "))
# numero02 = int(input("Digite o segundo numero: "))
# resultado = numero01 + numero02
# print(f"O resultado da soma entre {numero01} e {numero02} é: {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero = int(input("Digite um numero: "))
# resultado = numero % 5
# print(f"O resto da divisão do numero {numero} por 5 é: {resultado}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero01 = int(input("Digite o primeiro numero: "))
# numero02 = int(input("Digite o segundo numero: "))
# resultado = numero01 * numero02
# print(f"O resultado da multiplicacao entre {numero01} e {numero02} é: {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero01 = int(input("Digite o primeiro numero: "))
# numero02 = int(input("Digite o segundo numero: "))
# resultado = numero01 // numero02
# print(f"O resultado da divisao inteira entre {numero01} e {numero02} é: {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input("Digite um numero: "))
# resultado = numero ** 2
# print(f"O quadrado do numero {numero} é: {resultado}")


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero01 = float(input("Digite o primeiro numero: "))
# numero02 = float(input("Digite o segundo numero: "))
# resultado = numero01 + numero02
# print(f"O resultado da soma entre {numero01} e {numero02} é: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero01 = float(input("Digite o primeiro numero: "))
# numero02 = float(input("Digite o segundo numero: "))
# resultado = (numero01 + numero02) / 2
# print(f"A media entre {numero01} e {numero02} é: {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
# resultado = base ** expoente
# print(f"A potencia de {base} elevado a {expoente} é: {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temp_celcius = float(input("Digite a temperatura em celcius: "))
# temp_fahrenheit = (temp_celcius * 1.8) + 32
# print(f"A temperatura em fahrenheit de {temp_celcius} celcius é: {temp_fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio_circulo = float(input("Digite o raio do circulo: "))
# area_circulo = math.pi * raio_circulo ** 2
# print(f"A area do circulo de raio {raio_circulo} é: {area_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string = input("Digite uma string: ")
# print(string.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome_usuario = input("Digite seu nome completo: ")
# print(nome_usuario.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase_usuario = input("Digite uma frase com espaços no início e no final: ")
# print(f"Frase original: -{frase_usuario}-, Frase sem espaços no início e no final: -{frase_usuario.strip()}-")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato dd/mm/aaaa: ")
# dia_mes_ano = data.split("/")
# print(f"Dia: {dia_mes_ano[0]}")
# print(f"Mês: {dia_mes_ano[1]}") 
# print(f"Ano: {dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string01 = input("Digite a primeira string: ")
# string02 = input("Digite a segunda string: ")
# print(string01 + " " + string02)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# boolean01 = input("Digite o primeiro booleano: ")
# boolean02 = input("Digite o segundo booleano: ")
# print(f"O resultado da operação AND entre {boolean01} e {boolean02} é: {boolean01 and boolean02}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# boolean01 = input("Digite o primeiro booleano: ")
# boolean02 = input("Digite o segundo booleano: ")
# print(f"O resultado da operação OR entre {boolean01} e {boolean02} é: {boolean01 or boolean02}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# boolean = input("Digite um booleano: ")
# print(f"O booleano invertido de {boolean} é: {not boolean}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# number01 = int(input("Digite o primeiro numero: "))
# number02 = int(input("Digite o segundo numero: "))
# print(f"Os numeros {number01} e {number02} {(number01 == number02) and 'sao' or 'nao sao'} iguais")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# number01 = int(input("Digite o primeiro numero: "))
# number02 = int(input("Digite o segundo numero: "))
# print(f"Os numeros {number01} e {number02} {(number01 != number02) and 'sao' or 'nao sao'} diferentes")

# #### try-except e if

# 21: Conversor de Temperatura
# print("Escolha a temperatura que deseja converter: ")
# print("1 - Celsius para Fahrenheit")
# print("2 - Fahrenheit para Celsius")
# opcao = int(input("Digite a opcao desejada: "))

# if opcao == 1:
#     celsius = float(input("Digite a temperatura em Celsius: "))
#     fahrenheit = (celsius * 1.8) + 32
#     print(f"A temperatura em Fahrenheit de {celsius} Celsius é: {fahrenheit}")
# elif opcao == 2:
#     fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
#     celsius = (fahrenheit - 32) / 1.8
#     print(f"A temperatura em Celsius de {fahrenheit} Fahrenheit é: {celsius}")    
# else:
#     print("Opcao invalida")


# 22: Verificador de Palíndromo
# palavra = input("Digite uma palavra: ")
# palavra_invertida = palavra[::-1]
# print(f"A palavra {palavra} {(palavra == palavra_invertida) and 'é' or 'nao é'} palindromo")

# 23: Calculadora Simples
print("Escolha a operação desejada: ")
print("1 - Soma")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")
opcao = int(input("Digite a opcao desejada: "))

if opcao == 1:
    num01 = float(input("Digite o primeiro numero: "))
    num02 = float(input("Digite o segundo numero: "))
    print(f"A soma entre {num01} e {num02} é: {num01 + num02}")
elif opcao == 2:
    num01 = float(input("Digite o primeiro numero: "))
    num02 = float(input("Digite o segundo numero: "))
    print(f"A subtracao entre {num01} e {num02} é: {num01 - num02}")
elif opcao == 3:
    num01 = float(input("Digite o primeiro numero: "))
    num02 = float(input("Digite o segundo numero: "))
    print(f"A multiplicacao entre {num01} e {num02} é: {num01 * num02}")
elif opcao == 4:
    num01 = float(input("Digite o primeiro numero: "))
    num02 = float(input("Digite o segundo numero: "))
    print(f"A divisao entre {num01} e {num02} é: {num01 / num02}")
else:
    print("Opcao invalida")


# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
