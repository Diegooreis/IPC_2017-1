#--------------------------------------------------------------------------
#Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
#Gabriel Barroso da Silva Lima 1715310011
#Felipe Eduardo Silva de Almeida 1715310031
#Frederico Victor Alfaia Rodrigues 
1515200030
#Diogo Duarte
#Felipe Guerreiro de Mello 1315120052
#Fa�a um Programa que pe�a dois n�meros e imprima o maior deles. 
#-------------------------------------------------------------------------------------

a = float(input("digite um valor"))

b = float(input("digite outro valor"))

if a>b:

    print(a, "� maior que" ,b)

else:

    if b>a:
        print(b, "� maior que", a)
    else:

        print(b, "e", a, "s�o iguais")