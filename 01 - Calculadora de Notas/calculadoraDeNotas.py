import random

feedbackRuim = ["Uma pena que isso aconteceu, estude e dê o máximo de você na próxima!", "Poxa, infelizmente você não foi aprovado, mas lembre-se de nunca desistir e tentar novamente assim que possível!", "Não deixe isso te abalar, use isso para te tornar mais forte e aprender com os erros. Levante a cabeça e continue estudando!"]
feedbackMédio = ["Na trave! Mas ainda é completamente possível recuperar! Estude mais que você vai conseguir!", "Por pouco! A aprovação está ao seu alcance. Dê o seu máximo para recuperar!", "Quase para a aprovação! Mas fique tranquilo, estude e revise que você vai conseguir!"]
feedbackÓtimo = ["Uau! Você está de parabéns por conquistar essa nota! só lembre de não se acomodar rsrsrs.", "Fantástico! Conseguiu uma boa nota, está de parabéns!", "Demais! Você foi muito bem com essas notas!"]
feedbackFantáticoPrint = ["Você merece demais! Parabéns pela dedicação e esforço, você foi exemplar!", "Simplesmente belíssimas notas você conquistou! O seu esforço foi notável, continue assim e irá muito longe! Parabéns."]

feedbackRuimPrint = random.choice(feedbackRuim)
feedbackMédioPrint = random.choice(feedbackMédio)
feedbackÓtimoPrint = random.choice(feedbackÓtimo)
feedbackFantáticoPrint = random.choice(feedbackFantáticoPrint)

def soma_total(nota1, nota2, nota3):
    return nota1 + nota2 + nota3

def divisao_soma(soma):
    return soma / 3

def resultado_média(média):
    if média <= 4:
        print("Status: REPROVADO!")
        print(feedbackRuimPrint)

    elif 4 < média <= 6.99:
        print("Status: RECUPERAÇÃO!")
        print(feedbackMédioPrint)

    elif 7 <= média <= 8.99:
        print("Status: APROVADO!")
        print(feedbackÓtimoPrint)

    elif 9 <= média <= 10:
        print("Status: APROVADO!")
        print(feedbackFantáticoPrint)

def main():
    while True:
        try:
            nota1 = float(input('Insira sua primeira nota: '))
            nota2 = float(input('Insira sua segunda nota: '))
            nota3 = float(input('Insira sua terceira nota: '))

            if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
                print(f"\nAs notas devem estar entre 0 e 10.")
                continue

            soma = soma_total(nota1, nota2, nota3)
            média = divisao_soma(soma)

            print(f"\nA soma total de suas notas é: {soma}")
            print(f"Sua média é: {média:.2f}\n")

            resultado_média(média)
            break

        except ValueError:
            print("Insira apenas números válidos.")
main()
