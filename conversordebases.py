num = int(input('Digite um número inteiro: '))
print('''Escolha uma das Três bases para conversão:
[1] - Binario
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Sua Opção: '))

if opcao == 1:
    print('Converter para binario -->')
    print('O número decimal {} é igual a {} em binario'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('Converter para Ocatal -->')
    print('O número decimal {} é igual a {} em Octal'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('Converter para Hexadecimal -->')
    print('O número decimal {} é igual a {} em Hexadecimal'.format(num,hex(num)[2:]))
else:
    print('Opção invalida. Tente Novamente')

