# Biblioteca com função de "aleatoriedade". Nesse código, ela vai funcionar escolhendo de maneira aleatória algum "feedback" previamente inserido aqui.
import random

# Strings com os "feedbacks" personalizados e determinados para cada nota.
feedbackRuim = ["Uma pena que isso aconteceu, estude e dê o máximo de você na próxima!", "Poxa, infelizmente você não foi aprovado, mas lembre-se de nunca desistir e tentar novamente assim que possível!", "Não deixe isso te abalar, use isso para te tornar mais forte e aprender com os erros. Levante a cabeça e continue estudando!"]
feedbackMédio = ["Na trave! Mas ainda é completamente possível recuperar! Estude mais que você vai conseguir!", "Por pouco, mas a aprovação é plenamente alcançável, dê o seu máximo pra recuperar!", "Quase para a aprovação! Mas fique tranquilo, estude e revise que você vai conseguir!"]
feedbackÓtimo = ["Uau! Você está de parabéns por conquistar essa nota! só lembre de não se acomodar rsrsrs.", "Fantástico! Conseguiu uma boa nota, está de parabéns!", "Demais! Você foi muito bem com essas notas!"]
feedbackFantáticoPrint = ["Você merece demais! Parabéns pela dedicação e esforço, você foi exemplar!", "Simplesmente belíssimas notas você conquistou! O seu esforço foi notável, continue assim e irá muito longe! Parabéns."]

# Uso da biblioteca nas strings, para poder "printar" quando rodar o código.
feedbackRuimPrint = random.choice(feedbackRuim)
feedbackMédioPrint = random.choice(feedbackMédio)
feedbackÓtimoPrint = random.choice(feedbackÓtimo)
feedbackFantáticoPrint = random.choice(feedbackFantáticoPrint)

# Função (def) para somar as três notas inseridas pelo usuário.
def soma_total(nota1, nota2, nota3):
    return nota1 + nota2 + nota3

# Função (def) onde o resultado final da "def soma_total" será dividido por três e assim, fazendo a média final do usuário.
def divisao_soma(soma):
    return soma / 3

# Função onde irá apresentar ao usuário o seu "status" e o seu "feedback" a partir do resultado final do cálculo das notas.
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
    # Caso o usuário digite NÚMEROS válidos, o looping encerra, e passará adiante, fazendo o cálculo e imprimindo as mensagens. Se for digitado algum número negativo ao maior que 10, vai "printar" uma mensagem informando que apenas númeors entre 0 e 10 são válidos e em seguida, os "inputs" aparecerão novamente.
    while True:
        # O "try" serve para "tentar" executar a seguinte sessão do código, se houver alguma exceção, passará para o "except"
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
            print(f"Sua média é: {média:.2f}\n")                # O ".2f" significa que só vai aparecer dois caracteres após a vírgula (ponto)

            resultado_média(média)
            break

        # Caso o usuário insira algum caractere que não seja número
        except ValueError:
            print("Insira apenas números válidos.")
main()
