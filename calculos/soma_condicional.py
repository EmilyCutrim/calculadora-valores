#Variaveis usadas para entrada de valores números "int(input)..."
valor_um = int(input('Digite o primeiro valor: '))
valor_dois = int(input('Digite o primeiro valor: '))

#Variavel criada para receber o caracter digitado do tipo string
simbolo = (input('Digite o simbolo de operação: '))

#Variaveis criadas para armazenar o tipo de operador calculo (+, -, *, /)
soma = str('+')
subtracao = str('-')
multiplicacao = str('*')
divisao = str('/')

# Se a variável "simbolo" for igual a variavel "soma" então eu faço uma soma
if simbolo == soma:
    #Variável "resultado" é igual o "valor_um" + "valor_dois"
    resultado = valor_um + valor_dois
    #Recuperando valor da variável "resultado" que é uma soma 
    print(f'{resultado}')

# Se a variável "simbolo" for igual a variavel "subtracao" então eu faço uma soma
if simbolo == subtracao:
    #Variável "resultado" é igual o "valor_um" - "valor_dois"
    resultado = valor_um - valor_dois
    #Recuperando valor da variável "resultado" que é uma soma 
    print(f'{resultado}')

# Se a variável "simbolo" for igual a variavel "multiplicacao" então eu faço uma soma
if simbolo == multiplicacao:
    #Variável "resultado" é igual o "valor_um" * "valor_dois"
    resultado = valor_um * valor_dois
    #Recuperando valor da variável "resultado" que é uma soma 
    print(f'{resultado}')

# Se a variável "simbolo" for igual a variavel "divisao" então eu faço uma soma
if simbolo == divisao:
    #Variável "resultado" é igual o "valor_um" / "valor_dois"
    resultado = valor_um / valor_dois
    #Recuperando valor da variável "resultado" que é uma soma 
    print(f'{resultado}')


