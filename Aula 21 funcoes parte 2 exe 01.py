def contador(i,f,p):
    """
    Faz a contagem e mostra na tela

    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c=i
    while c<=f:
        print(f'{c}  ', end='')
        c +=p
    print('FIM')

contador(2,10,2)

help(contador)