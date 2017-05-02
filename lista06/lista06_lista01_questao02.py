#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
cont = 0

while (cont < 10):
    number = float(input("Digite um número: "))
    vetor.append(number)
    cont = cont + 1
print ("A ordem inversa é",vetor[::-1])
