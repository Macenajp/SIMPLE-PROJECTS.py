'''
Fatiamento de strings:

012345678
Hello World
-987654321

Fatiamento [i:f:p] [::]
Obs.: A função len retorna a quantidade de caracteres da str
'''

var = 'Hello World'
print(var[1])             # Vai "printar" apenas a letra "e" (a segunda - se, a variável for 1)

var = 'Hello World'
print(var[1:4])           # Vai "printar" a partir do primeiro índice escolhido até o último

var = 'Hello World'
print(var[:5])            # Omite o início e vai "printar" até o último índice

var = 'Hello World'
print(len(var))           # Contagem de caracteres

var = 'Hello World'
print(len(var[0:10]))     # Contagem de caracteres (de um ponto inicial até o final)

var = 'Hello World'
print(var[0:10:2])        # Contagem de números, contudo, o terceiro número escolhido funcionará na contagem para conta de N em N (EX. Se for [n:n:2], a contagem ocorrerá de dois em dois)

var = 'Hello World'
print(var[-1:-10:-1])     # "Printará" a variável de maneira invertida, seguindo a mesma lógica dos métodos anteriores
