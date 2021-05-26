#crie um programa que tenha uma tuplatotalmente preenchida com uma contagem por extenso de zero a 10. Seu progrma deverá ler um numero entre 0 e 10 e mostra-lo por extenso

cont=('zero', 'um','dois','tres','quatro', 'cinco', 'seis','sete', 'oito',
      'nove','dez')
while True:
    num=int(input('Leia um numero de 0 a 10: '))
    if 0<=num<=10:
        break

    #print('O numero digitado é :  {}' .format(num))

print(f'Voce digitou o numero {cont[num]}')