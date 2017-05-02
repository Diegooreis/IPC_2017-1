# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# André Luis Laborda Neves              1715310059
# João Vitor de Cordeiro B. Gonçalves   1515140036
# Gabriel Nascimento de Oliveira        1715310052
# Diego Reis figueira                   1515070169
# Diogo Roberto Duarte da Costa         1715310056


#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.Após isto, calcule a média anual das
temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperature = []
months = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
average = 0
aboveaverage= []
for i in range(len(months)):
 	  temperature.append(float(input('Informe a Temperatura media de ' + months[i] + ':\n')))
 	  average = (average + temperature[i])
average = average/len(months)

for i in range(len(months)):
 	  if(temperature[i] > average):
 		aboveaverage.update({months[i] : temperature[i]})

print('Media das temperaturas : Anual -> ' + str(average))
print('Meses com temperaturas acima da media: ' + str(aboveaverage))

