#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
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
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#  Ex.: 5!=5.4.3.2.1=120
#----------------------------------------------------------------------------

n = int(input("Informe um número: "))
cont = 1
fat = 1
while cont <= n:
    fat = fat*cont
    cont = cont+1
print(fat)
