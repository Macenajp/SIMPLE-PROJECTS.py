'''
Formatação de strings com f-strings:

s - string
d - intf
f - float

(Caractere)(><^)(quantidade)
.<quantidade de digitos>f
x ou X - Hexadecimal

> - Esqueda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros

Sinal - + ou -
Ex.: 0>-100,.1f

Conversion flags - !r !s !a
'''


var = 'ABC'

print(f'{var}')
print(f'{var: >10}') #Empurrará n caracteres para a direita
print(f'{var: <10}') #Fará o mesmo, mas, para a esquerda
print(f'{var: ^10}') #No caso, vai dividir a quantidade para cada um dos lados - mantendo ao máximo um equilíbrio
print(f'O hexadecial de 1500 é {1500:08X}')
print(f'{var!r}')
