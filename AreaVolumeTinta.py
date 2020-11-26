altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da partida? '))
area = altura * largura
print('Área da parede = ',area)
print('1 Litro de tinta pinta 2 metros quadrados')
litros = area/2
print('com uma area de {:.1f} você vai precisar de {:.1f} litros de tinta'.format(area,litros))