10
#Enunciado ex-78: faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final mostre qual foi o maior
# valor e o menor valor digitado e as suas respevtiaso posiçoes na lista.
listanum = []
maior=0
menor=0
for c in range(0,7):
    listanum.append(int(input(f'Digite um valor para a posição {c}:  ')))
    if c==0:
        maior=menor=listanum[0]
    else :
        if listanum[c] > maior:
            maior=listanum[c]
        if listanum[c] < menor:
            menor=listanum[c]

print(f'Vejamos como ficou a lista preenchida {listanum}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum): # percorre a lista da esquerda para a direita associando chave x valor
    if v==maior:
        print(f'{i}....',end='')
print()

print(f'O menor valor digitado foi {menor} nas posições  ', end='')
for i, v in enumerate(listanum): # percorre a lista da esquerda para a direita associando chave x valor
    if v==menor:
        print(f'{i}....',end='')
print()

