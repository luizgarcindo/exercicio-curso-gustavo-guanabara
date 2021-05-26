dados =dict()
dados = {'nome':'pedro','idade':25, 'altura':1.40}
print(dados['nome'])
print(dados['idade'])
del dados['idade']

print (dados)
dados['idade']=24
print(dados)
print(dados.values())
print(dados.keys())
print(dados.items())
for k,v in dados.items():
    print(f'O {k} é {v}')
#alterando valor de um campo
dados['nome']='joao'
print(dados)