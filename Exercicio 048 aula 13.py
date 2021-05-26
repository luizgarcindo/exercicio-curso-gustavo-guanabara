
# soma de numeros impares de 1 0 500 divisiveis por 3 - contar quantos numeros nesta condição.
soma=0
contador = 0
for c in range(1,501,2):
    if c%3 ==0:
        soma +=c
        contador +=1
        print(c, end = ' ')
print( 'A soma de todos os {} solicitados é  {}'. format(soma,contador))