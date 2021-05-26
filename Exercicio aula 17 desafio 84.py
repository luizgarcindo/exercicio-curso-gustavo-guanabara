temp = []
principal = []
mai = men = 0
while True:
    #lendo numa area temporaria temp
    temp.append(str(input(' nome: ')))
    temp.append(float(input('peso:  ')))
    # Cadastrando no cadastro principal
    # Se nao cadastrei ninguem ainda faço mai = men = temp[1]
    if len(principal)==0:
        mai = men = temp[1]
    else :
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar?? [S/N]'))
    if resp in 'Nn':
        break

print ('-+='*30 )
print(f' Os dados foram: {principal}')
print(f' Ao todo foram cadastrados {len(principal)} pessoas ')
print(f' O maior peso foi de {mai} KG, peso de  ' , end='')
for p in principal:
    if p[1] ==mai:
        print(f'[{p[0]}] ', end='')
print()
print(f' O menor peso foi de {men}  KG, peso de  ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}] ' , end='')
print()


