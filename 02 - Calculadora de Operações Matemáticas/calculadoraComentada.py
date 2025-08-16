# Biblioteca que será usada para gerar "delay" durante a execução de determinadas partes do código, deixando mais fluido
from time import sleep

# Sessão onde o usuário vai escolher o tipo de operação matemática (ou sair da execução).
def seleçãoDeOperação():
    print("Qual o tipo de operação que você quer fazer. \n0 -> Sair \n \n1 -> Soma",(" ") * 12, "5 -> Divisão inteira \n2 -> Subtração", (" ") * 7, "6 -> Resto de uma divisão \n3 -> Divisão comum", (" ") * 3, "7 -> Exponenciação \n4 -> Multiplicação")
    return int(input("\nEscolha: "))

# Função para somar os dois números escolhidos.
def soma(numero1, numero2):
    return numero1 + numero2

# Função para calcular a subtração.
def subtração(numero1, numero2):
    return numero1 - numero2

# Calcula a divisão entre os dois números.
def divisão(numero1, numero2):
    return numero1 / numero2

# Função para calcular a multiplicação.
def multiplicação(numero1, numero2):
    return numero1 * numero2

# Calcula divisão inteira dos dois números escolhidos.
def divInteira(numero1, numero2):
    return numero1 // numero2

# Função que calcula o resto da divisão dos números escolhidos.
def restoDaDivisão(numero1, numero2):
   return numero1 % numero2

def exponenciação(numero1, numero2):
   return numero1 ** numero2

# Sessão principal, onde tudo o que aparece para o usuário passa por aqui.
def main():
    # O while serve para o código ficar rodando infinitamente, até o usuário querer encerrar.
    while True:
        try:
            escolha = seleçãoDeOperação()

            # Para sair da execução:
            if escolha == 0:
                print("Obrigado por testar essa calculadora, volte sempre!")
                sleep(1) # Vai gerar um "delay" de 1 segundo
                break

            # Para a soma:
            if escolha == 1:
                print("Muito bem, você escolheu 'soma'. Quais números você quer somar?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {soma(numero1, numero2):.2f}")
                print("============================================\n")
                continue

            # Para a subtração:
            elif escolha == 2:
                print("Muito bem, você escolheu 'subtração'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {subtração(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # Para a divisão comum:
            elif escolha == 3:
                print("Muito bem, você escolheu 'divisão comum'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                if numero2 == 0:        # Foi inserido esse "if" para o o usuário não digitar o "0", justamente para evitar mensagens de "Error".
                    print("\nImpossível com esse número.\n")
                    print("====================================\n")
                    continue
                print(f"\nO resultado é: {divisão(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # Para a multiplicação:
            elif escolha == 4:
                print("Muito bem, você escolheu 'multiplicação'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {multiplicação(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # Para a divisão inteira:
            elif escolha == 5:
                print("Muito bem, você escolheu 'divisão inteira'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                if numero2 == 0:        # Foi inserido esse "if" para o o usuário não digitar o "0", justamente para evitar mensagens de "Error".
                    print("\nImpossível com esse número.\n")
                    print("====================================\n")
                    continue
                print(f"\nO resultado é: {divInteira(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # Para saber o resto de uma divisão:
            elif escolha == 6:
                print("Muito bem, você quer saber o 'resto de uma divisão'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                if numero2 == 0:        # Foi inserido esse "if" para o o usuário não digitar o "0", justamente para evitar mensagens de "Error".
                    print("\nImpossível com esse número.\n")
                    print("====================================\n")
                    continue
                print(f"\nO resultado é: {restoDaDivisão(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            elif escolha == 7:
                print("Muito bem, você quer saber o resultado de uma exponenciação. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {exponenciação(numero1, numero2):.2f}")
                print("====================================\n")
                continue


            else:
                print("\nEscolha uma das opções oferecidas!")
                continue

            break
        except ValueError:
            print("Escolha um valor válido (entre 0 e 7)!")
main()
