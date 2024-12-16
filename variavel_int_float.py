print('\n\nVariáveis Numéricas - Float e Int')
variavel_tipo_int = 10
variavel_tipo_float = float(variavel_tipo_int)
print(f"O tipo da variável variavel_tipo_int ({variavel_tipo_int}) é {type(variavel_tipo_int)}")
print(f"O tipo da variável variavel_tipo_float ({variavel_tipo_float}) é {type(variavel_tipo_float)}")
outro_float = 1.99
print(outro_float)
print(type(outro_float))
outro_int = int(outro_float) # pegou a parte INTEIRA do float (a parte ANTES do .)
print(outro_int)
print(type(outro_int))
print(round(outro_float)) # arredondou conforme regras matemáticas = se o primeiro número depois do ponto for de 0 a 4, arredonda para menos, se entre 5 e 9, para mais
numero_string = input('Digite um número')
print(type(numero_string))
numero_convertido_para_int = float(numero_string)
print(type(numero_convertido_para_int))
