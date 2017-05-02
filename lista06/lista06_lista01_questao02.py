#---------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr

# Diego Reis Figueira      		      	1515070169
# André Luis Laborda Neves            	1515070006
# Gabriel Nascimento de Oliveira  	  	1715310052
# Diogo Roberto Duarte da Costa 	  	1715310056
# João Vitor de Cordeiro B. Gonçalves 	1515140036


#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
cont = 0

while (cont < 10):
    number = float(input("Digite um número: "))
    vetor.append(number)
    cont = cont + 1
print ("A ordem inversa é",vetor[::-1])
