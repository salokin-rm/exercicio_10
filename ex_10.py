"""
Nome: Equação de 2º Grau
Descrição: Solicita o valor de um capital, o prazo de investimento, a taxa de juros, calcula e imprime na tela o valor capitalizado.
Autor: Nikolas
Versão: 0.0.1
Data: 27/06/2023

"""

#Atribuição de Variáveis

"""
Ci   -> Capital Inicial
Cf   -> Capital Final
P    -> Prazo em dias
J    -> Juros anuais
Jdia -> Juros diários
R    -> Retorno Bruto

"""


#Entrada de Dados


Ci = float(input("\nQual o valor inicial do capital?"))
P  = float(input("\nQual o prazo do investimento (em dias)?"))
J  = float(input("\nQual a taxa de juros (% a.a.)?"))



#Processamento de Dados
                 

    
    
Jdia = (J/100)/365
R = Ci*Jdia*P
Cf = Ci + Ci*Jdia*P                 

                 
#Saída de Dados
                
print("\nCapital inicial: R$",Ci,".")
print("\nPrazo do investimento:",P,"dia(s).")
print("\nTaxa de juros:",J,"% a.a.")
print("\nRetorno bruto: R$",round(R,2),".")
print("\nCapital final: RS$",round(Cf,2),".")