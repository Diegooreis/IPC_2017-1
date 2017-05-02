# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# André Luis Laborda Neves              1515070006 
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Gabriel Nascimento de Oliveira        1715310052
# Diego Reis figueira                   1515070169
# Diogo Roberto Duarte da Costa         1715310056

#Escreva um algoritmo em PORTUGOL que armazene em um vetor todos os números inteiros do intervalo fechado de 1 a 100. Após isso, o algoritmo deve imprimir todos
#os valores armazenados.


vetor = []
cont = 0
number = 1
while (cont < 100):
    if (number != 0):
        vetor.append(number)
        number= number + 1
        cont = cont + 1
print (vetor)
