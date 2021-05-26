try:
    a=int(input('Numerador:  '))
    b=int(input('Denominador:   '))
    r=a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    Print('Não é possivel dividir um numero por zero! ')
except keyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')
except Exception as erro:
    print('O erro encontrado foi {erro._cause_}')
else:  #caso esteja certo
    print(f'O resultado foi {r:.1f}')
finally:  #em todos os casos
    print('Volte sempre - obrigado')