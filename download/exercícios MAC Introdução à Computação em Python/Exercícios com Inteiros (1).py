#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""""
Exercícios ime-USP

""""


# In[29]:


# 1.  Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.

print('Quadrado de uma sequencia de números digitados.\n')
print('A sequência termina digitando 0 (zero).\n')

num = int(input('Digite um número: '))

while num != 0:
    quadrado = num * num
    print(num, 'ao quadrado de é', quadrado)
    num = int(input('Digite um número: '))
    


# In[8]:


#2.  Dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos.

print('Soma dos n primeiros inteiros')

num = int(input('Digite o valor do número desejado: '))
# num vai ser a sequencia de números para haver a soma

soma = 0
i = 1
while i <= num:
    soma = soma + i
    i = i + 1
    
print('A soma dos', num, 'primeiros inteiros positivos é', soma)

