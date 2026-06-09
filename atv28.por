programa {
  funcao inicio() {
  real teste, prova, media
    inteiro faltas

    escreva("Digite a nota do teste: ")
    leia(teste)

    escreva("Digite a nota da prova: ")
    leia(prova)

    escreva("Digite a quantidade de faltas: ")
    leia(faltas)

    media = (teste + prova) / 2

    escreva("\nMedia: ", media, "\n")

    se (media >= 7.0 e faltas < 10)
    {
        escreva("Aprovado")
    }
    senao se (media >= 5.0 e media <= 6.9 e faltas < 10)
    {
        escreva("Recuperacao")
    }
    senao
    {
        escreva("Reprovado")
    }
  }
}
