temperature = []
months = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
average = 0
aboveaverage= {}
for i in range(len(months)):
	temperature.append(float(input('Informe a Temperatura media de ' + months[i] + ':\n')))
	average = (average + temperature[i])
average = average/len(months)

for i in range(len(months)):
	if(temperature[i] > average):
 		aboveaverage.update({months[i] : temperature[i]})

print('Media das temperaturas : Anual -> ' + str(average))
print('Meses com temperaturas acima da media: ' + str(aboveaverage))