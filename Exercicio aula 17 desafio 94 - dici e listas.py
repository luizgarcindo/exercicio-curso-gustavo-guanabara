#Neste desafio sao lidos dados de pessoas (nome, idade e sexo) guardando os dados de cada  pessoa em um dicionario
# e todos os dicionarios em uma lista. No final mostra:a) quantas pessoas cadastradas,b) a media de idade, c) uma
#lista com mulheres, d) uma lista com a idade acima da media.

galera = list()
pessoa = dict()
somaIdade=0
numeroMulheres=0
while True:
    pessoa.clear
    # Cadastrando nome
    pessoa['nome']= str(input('nome:  '))

    #cadastrando sexo
    while True:
             pessoa['sexo']= str(input('Sexo: [M/F] ')).upper()[0]
             if pessoa['sexo'] in 'MF':
                break
             print(f'erro  Por favor digite M ou F')

    #cadastrando idade
    pessoa['idade']= int(input('Digite a idade da pessoa:   '))
    somaIdade+= pessoa['idade']
    #copiando registro(dic) para lista galera
    galera.append(pessoa.copy()) #copiando registro(dicio) para lista galera
    while True:
        resposta = str(input('Quer continuar?  [S/N')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO..reponda S ou N')
    if resposta == 'N':
        break
print(galera)
print('+='*30)
print(f'Item A - Pessoas cadastradas:  {len(galera)} ')
mediaIdades= somaIdade/len(galera)
print(f'Item B - a media das idades é: {mediaIdades:5.2f} anos.  ')
print(f' Item C - As mulheres cadastradas foram :   ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(' Item D - Lista de pessoas que tem idade maior que a media de idades')
for p in galera:
    if p['idade'] >= (somaIdade/len(galera)):
        print('                  ')
        for k,v in p.items():
            print(f'{k} = {v};  ',end='')
        print()
print('ENCERRADO PROCESSO')




