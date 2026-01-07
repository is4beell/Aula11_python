import os
import random

def gerar_numeros(ini, fim, qtd):
    lst_num = [random.randint(ini, fim) for i in range(qtd)]
    return lst_num


def somar(num1, num2):
    soma = (num1 + num2)
    return soma

def multiplica(num1, num2):
    multiplica = (num1 * num2)
    return multiplica

def subtrai(num1, num2):
    subtrai = (num1 - num2)
    return subtrai

def divide(num1, num2):
    divide = (num1 / num2)
    return divide

inicio = 1
final = 10
quantidade = 2
lst_numeros = gerar_numeros(inicio, final, quantidade)
print(lst_numeros)


soma_numeros = somar(lst_numeros[0], lst_numeros[1])
print(soma_numeros)

multiplica = multiplica(lst_numeros[0], lst_numeros[1])
print(multiplica)

subtrai = subtrai(lst_numeros[0], lst_numeros[1])
print(subtrai)

divide = divide(lst_numeros[0], lst_numeros[1])
print(divide)



