#---------------------------------------------------------------------------
# Introdu��o a Programa��o de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Adham Lucas da Silva Oliveira           1715310059
# Gabriel Barroso da Silva Lima           1715310011
# Guilherme Silva de Oliveira             1715310034
# Nat�lia Cavalcante Xavier               1715310021
# Tiago Ferreira Aranha	                  1715310047
#
# Dada uma seq��ncia de n n�meros, imprimi-la na ordem inversa � da leitura. 
#---------------------------------------------------------------------------

n = int(input("digite a quantidade de n�meros: "))
lista = []

for i in range (0, n):
    
    numero = int(input("digite um n�mero: "))
    lista.append(numero)
    
while n > 0:
    
    n -= 1
    print (lista[n])