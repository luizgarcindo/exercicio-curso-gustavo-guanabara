def voto(ano):
    from datetime import date
    atual= date.today().year
    idade=atual - ano
    if idade >= 60:
        tipoVoto='o voto é opcional'
    else:
        if idade <= 16:
            tipoVoto= 'negado - não vota'
        else:
            tipoVoto='voto obrigatório'
    return tipoVoto


#nota - no return poderia ser usado ....return  f'mensagem de retorno'

nome=str(input(' Digite o nome da pessoa:      '))
anonascimento=int(input('Digite o ano de nascimento da pessoa:   '))
r1= voto(anonascimento)
print(f' A pessoa de nome {nome} tem voto {r1}  ')
print(f'A pessoa de nome {nome} tem voto {voto(anonascimento)} ')






