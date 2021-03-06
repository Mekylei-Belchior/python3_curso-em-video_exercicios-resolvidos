"""
 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
 A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
 a soma entre todos os valores pares sorteados pela função anterior.

"""

from random import randint


def sorteia(lista):

    for i in range(0, 5):
        numeros.append(randint(0, 100))


def somaPar(lista):

    resultado = 0

    for num in lista:

        if num % 2 == 0:
            resultado += num

    print(f'Valores sorteados: {lista}')
    print(f'A soma dos valores pares sorteados é: {resultado}')


numeros = []
sorteia(numeros)
somaPar(numeros)
