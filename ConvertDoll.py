reais = float(input('quantos reais vc tem? '))
dolars = reais / 3.27
print('com R${:.2f} você pode comprar US${:.2f}'.format(reais,dolars))