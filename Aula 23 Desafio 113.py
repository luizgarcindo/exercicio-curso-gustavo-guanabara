# programa lendo dados e pegando erros diversos

def leiaInt(msg): # modulo para ler numero inteiro com avaliação de consistencia
    while True:
        try:
            n=int(input(msg))
        except(ValueError, TypeError):# se houver digitação errada
            print('Erro: por favor digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('usuario preferiu nao digitar este numero')
            return 0
        else:    # se estiver ok
            return n

def leiaFloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError, TypeError):  # se houver digitação errada
            print('Erro: por favor digite um numero real valido')
            continue
        except(KeyboardInterrupt):
            print('usuario preferiu nao digitar este numero')
            return 0
        else:  # se estiver ok
            return n






num=leiaInt('Digite um valor inteiro:   ')
print(f' O valor digitado foi: {num}')

nfloat=leiaFloat('Digite valor real:  ')
print(f'O valor digitado foi:   {nfloat}')