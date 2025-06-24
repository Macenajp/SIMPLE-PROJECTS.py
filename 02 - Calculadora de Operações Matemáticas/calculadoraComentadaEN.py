# Library that will be used to generate "delay" during the execution of certain parts of the code, making it more fluid
from time import sleep

# Session where the user will choose the type of mathematical operation (or exit execution)
def seleçãoDeOperação():
    print("Qual o tipo de operação que você quer fazer. \n0 -> Sair \n1 -> Soma \n2 -> Subtração \n3 -> Divisão comum\n4 -> Multiplicação \n5 -> Divisão inteira \n6 -> Resto de uma divisão")
    return int(input("\nEscolha: "))

# Function to add the two numbers chosen
  def soma(numero1, numero2):
    return numero1 + numero2

# Function to calculate subtraction
    def subtração(numero1, numero2):
    return numero1 - numero2

# Calculates the division between the two numbers
    def divisão(numero1, numero2):
    return numero1 / numero2

# Function to calculate multiplication
    def multiplicação(numero1, numero2):
    return numero1 * numero2

# Calculates integer division of the two chosen numbers
    def divInteira(numero1, numero2):
    return numero1 // numero2

# Function that calculates the remainder of the division of the chosen numbers
def restoDaDivisão(numero1, numero2):
   return numero1 % numero2

# Main session, where everything that appears to the user passes through here.
  def main():
    # The while is used to keep the code running infinitely, until the user wants to terminate it.
    while True:
        try:
            escolha = seleçãoDeOperação()

            # To exit execution::
            if escolha == 0:
                print("Obrigado por testar essa calculadora, volte sempre!")
                sleep(1) # Vai gerar um "delay" de 1 segundo
                break

            # For the sum:
            if escolha == 1:
                print("Muito bem, você escolheu 'soma'. Quais números você quer somar?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {soma(numero1, numero2):.2f}")
                print("============================================\n")
                continue

            # For subtraction:
            elif escolha == 2:
                print("Muito bem, você escolheu 'subtração'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {subtração(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # For the common division:
            elif escolha == 3:
                print("Muito bem, você escolheu 'divisão comum'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                if numero2 == 0:        # This “if” has been inserted so that the user doesn't type ‘0’, precisely to avoid “Error” messages.
                    print("\nImpossível com esse número.\n")
                    print("====================================\n")
                    continue
                print(f"\nO resultado é: {divisão(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # For multiplication:
            elif escolha == 4:
                print("Muito bem, você escolheu 'multiplicação'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                print(f"\nO resultado é: {multiplicação(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # For integer division:
            elif escolha == 5:
                print("Muito bem, você escolheu 'divisão inteira'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                if numero2 == 0:        # This “if” has been inserted so that the user doesn't type ‘0’, precisely to avoid “Error” messages.
                    print("\nImpossível com esse número.\n")
                    print("====================================\n")
                    continue
                print(f"\nO resultado é: {divInteira(numero1, numero2):.2f}")
                print("====================================\n")
                continue

            # To find the remainder of a division:
            elif escolha == 6:
                print("Muito bem, você quer saber o 'resto de uma divisão'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                sleep(1)
                if numero2 == 0:        # This “if” has been inserted so that the user doesn't type ‘0’, precisely to avoid “Error” messages.
                    print("\nImpossível com esse número.\n")
                    print("====================================\n")
                    continue
                print(f"\nO resultado é: {restoDaDivisão(numero1, numero2):.2f}")
                print("====================================\n")
                continue


            else:
                print("\nEscolha uma das opções oferecidas!")
                continue

            break
        except ValueError:
            print("Escolha um valor válido (entre 0 e 6)!")
main()
