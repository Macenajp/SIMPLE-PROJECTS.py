# Library with "randomization" function. In this code, it will work by randomly choosing some feedback previously entered here.
import random

# Strings with the customized and determined "feedbacks" for each note.
feedbackRuim = ["Uma pena que isso aconteceu, estude e dê o máximo de você na próxima!", "Poxa, infelizmente você não foi aprovado, mas lembre-se de nunca desistir e tentar novamente assim que possível!", "Nào deixe isso te abalar, use isso para te tornar mais forte e aprender com os erros. Levante a cabeça e continue estudando!"]
feedbackMédio = ["Na trave! Mas ainda é completamente possível recuperar! Estude mais que você vai conseguir!", "Por pouco, mas a aprovação é plenamente alcançável, dê o seu máximo pra recuperar!", "Quase para a aprovação! Mas fique tranquilo, estude e revise que você vai conseguir!"]
feedbackÓtimo = ["Uau! Você está de parabéns por conquistar essa nota! só lembre de não se acomodar rsrsrs.", "Fanstástico! Conseguiu uma boa nota, está de parabéns!", "Demais! Você foi muito bem com essas notas!"]
feedbackFantáticoPrint = ["Você merece demais! Parabéns pela dedicação e esforço, você foi exemplar!", "Simplesmente belíssimas notas você conquistou! O seu esforço foi notável, continue assim e irá muito longe! Parabéns."]

# Use of the library in the strings, to be able to "print" when running the code.
feedbackRuimPrint = random.choice(feedbackRuim)
feedbackMédioPrint = random.choice(feedbackMédio)
feedbackÓtimoPrint = random.choice(feedbackÓtimo)
feedbackFantáticoPrint = random.choice(feedbackFantáticoPrint)

# Function (def) to add up the three notes entered by the user.
def soma_total(nota1, nota2, nota3):
    return nota1 + nota2 + nota3

# Function (def) where the final result of "def soma_total" will be divided by three and thus make the user's final average.
  def divisao_soma(soma):
    return soma / 3

# This function will show the user their “status” and their “feedback” from the final result of the grade calculation.
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
    # The “try” is used to ‘try’ to execute the following section of code, if there is an exception, it will be passed to the “except”.
    try:
        nota1 = float(input('Insira sua primeira nota: '))
        nota2 = float(input('Insira sua segunda nota: '))
        nota3 = float(input('Insira sua terceira nota: '))

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
            print("As notas devem estar entre 0 e 10.")
            return

        soma = soma_total(nota1, nota2, nota3)
        média = divisao_soma(soma)

        print(f"\nA soma total de suas notas é: {soma}")
        print(f"Sua média é: {média:.2f}\n")

        resultado_média(média)

  # If any value entered by the user is negative, or is greater than “10”, this message will appear on the console.
    except ValueError:
        print("Insira apenas números válidos.")
main()
