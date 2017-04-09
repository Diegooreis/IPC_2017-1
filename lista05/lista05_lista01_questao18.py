# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey         1715310059
# Edson de Lima Barros          1715310043
# Enrique Leão Barbosa Izel     1715310048
# Diego Reis figueira           1515070169
# Diogo Roberto Duarte da Costa 1715310056
# Iury da Silva Coelho          1715310069
#
#18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
#-----------------------------------------------------------------------------------------------------------------------

amount= float(input('Quantidade de numeros:'))
number= float(input('digite outro nuemro:'))
larger= number
smaller= number
x= 1
while (x < amount):
    number= float(input('digite outro nuemro:'))
    if (number > larger):
        larger= number
        number= number + 1
        x= x + 1
    else:
        (number < smaller)
        smaller= number

print('o maior valor eh', larger)
print('o menor valor eh', smaller)
print('a soma dos valores eh:', larger + smaller)
