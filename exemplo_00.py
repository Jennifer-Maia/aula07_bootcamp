## SEM FUNÇÃO!
# valor_1 = 4 
# valor_2 = 6 

# valor_3 = valor_1 + valor_2

# valor_4 = 6
# valor_5 = 4

# valor_6 = valor_4 + valor_5

valor_1 = 4
valor_2 = 6

def soma(valor_1_para_somar:float, valor_2_para_somar:float) -> float:
    #Doc string: diz o que essa função faz.
    """
    Uma função simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma
#soma(valor_1, valor_2) #Posso fazer assim ou declarando a variavel
valor_3 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2) #Declando a variavel

print(valor_3)