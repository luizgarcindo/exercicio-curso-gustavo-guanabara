kilometros = float(input('quantos kilometros percorreu?  '))
dias = float(input('quantos dias usou o carro? '))
preço = 60*dias+(0.15* kilometros)
print('O preço a pagar por {} quilometros rodados e uso de {} dias é de R$ {} '.format(kilometros,dias,preço))
