#gerenciamento de um jogador de futebol
time=list()
jogador=dict()
partidas=list()
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome do jogador:   '))
    tot=int(input(f'Quantas partidas {jogador["nome"]} jogou??'))
    for c in range(0,tot):
        partidas.append(int(input(f'  Quantos gols na partida {c}??   ')))
    jogador['gols']= partidas[:]# copiando gols por partida no atributo gols
    jogador['Total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta= str(input('Quer continuar??   [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO   Responda apenas S ou N.')
        if resposta=='N':
            break
    print('+='*30)
    print(jogador)
    print('+='*30)
    for k,v in jogador.items():
        print(f"O campo {k} tem o valor {v}")
    print('+='*30)
    for i, v in enumerate(jogador['gols']):
        print(f'  ====> na partida {i} fez {v}gols.')
    print(time)
