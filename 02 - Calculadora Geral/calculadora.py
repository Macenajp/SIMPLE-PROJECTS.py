def seleçãoDeOperação():
    print("Qual o tipo de operação que você quer fazer. \n1 -> Soma \n2 -> Subtração \n3 -> Multiplicação \n4 -> Divisão")
    return int(input("\nEscolha: "))


def main():
    while True:
        try:
            escolha = seleçãoDeOperação()

            if escolha == 1:
                print("Muito bem, você escolheu 'soma'. Quais números você quer somar?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                print("\nO resultado é: ", numero1 + numero2)
                print("============================================\n")
                return seleçãoDeOperação()


            elif escolha == 2:
                print("Muito bem, você escolheu 'subtração'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                print("\nO resultado é: ", numero1 - numero2)
                print("====================================\n")
                return seleçãoDeOperação()


            elif escolha == 3:
                print("Muito bem, você escolheu 'multiplacação'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                print("\nO resultado é: ", numero1 * numero2)
                print("====================================\n")
                return seleçãoDeOperação()


            elif escolha == 4:
                print("Muito bem, você escolheu 'divisão'. Quais números você quer usar no cálculo?")
                numero1 = int(input("Primeiro número: "))
                numero2 = int(input("Segundo número: "))
                print("\nO resultado é: ", numero1 / numero2)
                print("====================================\n")
                return seleçãoDeOperação()


        except ValueError:
            print("Escolha um valor válido (entre 1 e 4)!")

main()
