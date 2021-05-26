galera = [['Luiz',75],['Joao',24],['Ana', 20]]
print(galera)
print(galera[0])
print(galera[1])
print(galera[0][0])
print(galera[0][1])
for pessoa in galera:#para cada no da lista galera escreva o conteudo do no
     print(pessoa)
for pessoa in galera:
     print(pessoa[0],pessoa[1])

# agora vou pegar no teclado alguns dados e armazenar na lista DADO. Em seguida copio para a lista GALERA e imprimo as
# pessoas com maior e menor de idade
dado = list()
totalmaiores = totalmenores = 0
for c in range (0,5):
     dado.append(str(input('Nome:   ')))
     dado.append(int(input('Idade:   ')))
     galera.append(dado[:])
     dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.  ')
        totalmaiores +=1
    else:
        print(f'{p[0]} é menor de idade. ')
        totalmenores +=1
print(f'Temos {totalmaiores} maiores e {totalmenores} menores de idade')






