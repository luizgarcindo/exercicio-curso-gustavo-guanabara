nome = str(input('nome da pessoa  '))
# nome com maiusculas
print('escrevendo nome com maiusculas ', nome.upper())
# nome com minusculas
print('Escrevendo nome com minusculas  ', nome.lower())
# quantas letras ao todo sem considerar espaços
numletras = len(nome)
print('Quantas letras ao todo' , numletras)
numbrancos = nome.count(' ')
print('Numero de brancos ', numbrancos)
print('Numero de letras sem espaços é de {} ' .format((numletras - numbrancos) ))
# Quantas letras tem o primeiro nome??
listanome = nome.split()
print(listanome)
print('O primeiro nome que aparede é ',listanome[0])
Exercicio 4