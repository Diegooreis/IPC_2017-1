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
#As Organiza��es Tabajara resolveram dar um aumento de sal�rio aos seus colaboradores e lhe contraram para desenvolver o programa que calcular� os reajustes.
#    Fa�a um programa que recebe o sal�rio de um colaborador e o reajuste segundo o seguinte crit�rio, baseado no sal�rio atual:
#    sal�rios at� R$ 280,00 (incluindo) : aumento de 20%
#    sal�rios entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    sal�rios entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    sal�rios de R$ 1500,00 em diante : aumento de 5% Ap�s o aumento ser realizado, informe na tela:
#    o sal�rio antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo sal�rio, ap�s o aumento.
#-------------------------------------------------------------------------------------

sal1 = float(input("digite um sal�rio"))

if sal1 <= 280:

    sal2 = sal1*1.2
    
    per = 20

else:
    
    if sal1 <= 780:
        
        sal2 = sal1*1.15
        
        per = 15
    
    else:
        
        if sal1 <= 1500:
            
            sal2 = sal1*1.1
            
            per = 10
        
        else:
     
            sal2 = sal1*1.05
            
            per = 5

dif = sal2 - sal1

print("sal�rio anterior: R$", sal1, "reais || sal�rio atual: R$", sal2, "reais")

print("percentual de aumento aplicado: ", per,"% || valor do aumento: R$", dif, "reais")