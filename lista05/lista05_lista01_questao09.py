#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Alexandre Marques Uchôa                 1715310028
# André Luís Laborda Neves                1515070006
# Carlos Eduardo Tapudima de Oliveira	  1715310030
# Aracille de Souza Barbosa               1315120206
# Dayana Picanço Marquez                  1715310058
#
#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
#----------------------------------------------------------------------------

count = 1

while 0 < count < 50:
    arith_progress = 1 + (count - 1)*1
    count += 1
    if (arith_progress % 2 != 0):
        print(arith_progress, end = '  ')
