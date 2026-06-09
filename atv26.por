programa {
  funcao inicio() {
    inteiro idade, tempoB, tempoC
        logico infracao

        escreva("Digite a idade: ")
        leia(idade)

        escreva("Anos de habilitacao B: ")
        leia(tempoB)

        escreva("Anos de habilitacao C: ")
        leia(tempoC)

        escreva("Teve infracao nos ultimos 12 meses? (true/false): ")
        leia(infracao)

        se (idade > 21 e
            (tempoB >= 2 ou tempoC >= 1) e
            infracao == falso)
        {
            escreva("Apto para categoria D")
        }
        senao
        {
            escreva("Nao apto para categoria D")
        }


  }
}
