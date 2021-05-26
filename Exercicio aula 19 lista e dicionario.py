#criando dicionario dentro de uma lista
brasil=[]
estado1={'uf':'Rio de janeiro', 'Sigla': 'RJ'}
estado2= {'Uf':'Sao paulo', 'Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['Sigla'])
print('+='*30)
for p in brasil:
    print(p)


