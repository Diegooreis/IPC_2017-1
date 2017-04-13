#----------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro De Mello         1315120052
# Silas castro de Mendon�a          1715310066
# A s�rie de FETUCCINE � gerada da seguinte forma: 
# os dois primeiros termos s�o fornecidos pelo usu�rio; 
# a partir da�, os termos s�o gerados com a soma ou 
# subtra��o dos dois termos anteriores, ou seja:
# A(i) = A(i-1) + A(i-2) para i �mpar
# A(i) = A(i-1) - A(i-2) para i par
# Criar um algoritmo em PORTUGOL que imprima 
# os N primeiros termos da s�rie de FETUCCINE, 
# sabendo-se que para existir esta s�rie ser�o 
# necess�rios pelo menos tr�s termos.

termo1 = int(input("primeiro termo: "))
termo2 = int(input("segundo termo: "))
N = int(input("quantidade de termos: "))
c = 2

if N == 1:
    
    print(termo1)
    
else:
    
    if N >= 2:
    
        print(termo1)
        print(termo2)

while c < N:
    
    c += 1
    save = termo2
    
    if c % 2 != 0:
        
        termo2 += termo1
        termo1 = save
        print(termo2)
        
    else:
        
        termo2 -= termo1
        termo1 = save
        print(termo2)