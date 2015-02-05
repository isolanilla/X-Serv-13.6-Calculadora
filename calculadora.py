#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Ejecución python calculadora.py funcion operando1 operando2
"""


import sys
import os

functions = ['sum', 'rest', 'mult', 'div']

if len(sys.argv) != 4:

    sys.exit("Error en el número de argumentos")


def mysum(parametro1, parametro2):

    return(parametro1 + parametro2)


def myrest(parametro1, parametro2):

    return(parametro1 - parametro2)


def mymult(parametro1, parametro2):

    return(parametro1 * parametro2)


def mydiv(parametro1, parametro2):
    try:
        return(parametro1/parametro2)
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        exit()

try:
    float(sys.argv[3])
    float(sys.argv[2])
except ValueError:
    print('could not convert string to float')
    exit()


if sys.argv[1] == functions[0]:

    print mysum(float(sys.argv[2]), float(sys.argv[3]))

elif sys.argv[1] == functions[1]:

    print myrest(float(sys.argv[2]), float(sys.argv[3]))

elif sys.argv[1] == functions[2]:

    print mymult(float(sys.argv[2]), float(sys.argv[3]))

elif sys.argv[1] == functions[3]:

    print mydiv(float(sys.argv[2]), float(sys.argv[3]))

else:

    print('funcion incorrecta ' + '|' + sys.argv[1] + '|')
