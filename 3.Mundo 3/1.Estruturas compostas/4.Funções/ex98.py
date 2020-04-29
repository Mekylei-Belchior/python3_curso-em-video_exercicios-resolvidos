"""
 Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
 início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

 a) de 1 até 10, de 1 em 1;
 b) de 10 até 0, de 2 em 2;
 c) uma contagem personalizada.

"""
from time import sleep


def contador(inicio, fim, passo):

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    msg = f'Contagem de {inicio} até {fim} de {passo} em {passo}'
    print('-' * len(msg))
    print(msg)

    if inicio < fim:
        cont = inicio

        while cont <= fim:

            print(cont, end=' ')
            sleep(0.5)

            cont += passo

        print()

    else:

        cont = inicio

        while cont >= fim:

            print(cont, end=' ')
            sleep(0.5)

            cont -= passo

        print()
    print('-' * len(msg))


contador(1, 10, 1)
contador(10, 0, 2)

print()
print('Agora é sua vez de personalizar a contagem.')
i = int(input('Início:    '))
f = int(input('Fim:       '))
p = int(input('Passo:     '))
contador(i, f, p)
