# Bibliotecas
import random
import os
#  random.randint -> Números inteiros 
n = random.randint(1, 10)
m = random.randint(1, 10)
#print(n,m)


# ------------------------------------------------------------------------------------
# Gerar números decimais 
n_decimal = random.uniform(1, 10)
numero_decimal = round(n_decimal, 1) # Arredonda 
print(f'{n_decimal: .2f}') # Formata para duas casas 
print(numero_decimal)



#-------------------------------------------------------------------------------------
# Gerar números aleatórios dentro de uma lista 
lst_numeros = [random.randint(1, 10) for num in range(5)]
os.system('cls')  #Limpa a tela antes de printar a lista 

print(lst_numeros)