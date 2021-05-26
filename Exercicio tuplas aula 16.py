lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print (lanche[1:])# pega de 1 a 3 - suco pizza pudim
print (lanche [-1])#pega -1 - pudim
print (lanche [-2])# pega -2 - pizza
print (lanche[-3])# pega -3 - suco
print(lanche[1:3])#pega do 1 até 2
print(lanche[0:4])#pega do zero ate o 3
print(lanche[:2])# pega do zero ate o 1
print(lanche[:1])# pega do zero ate zero
print(30*'_')
for comida in lanche:
    print('Eu vou comer {}'.format(comida))
print(30 * '_')
#comando print de outra forma
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(30*'-')
#classificar tupla e imprimir
print(sorted(lanche))
print(30*'-')
# operações com tuplas
a=(2,5,6,7,8)
b=(8,9, 10)
c=a+b #concatenou tuplas
print (c)
# for com range
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print(30*'-')
# for sem range
for comida in lanche:
    print(f"Eu vou comer {comida}")

# outras propriedades de tuplas - concatenação
# index ___> posição na tupla
a= (2,5,8)
b=(9, 10, 1, 2)
c= a+b
print(c)
print(c.index(5))
#pytin aceita tuplas com dados com tipos diferentes


