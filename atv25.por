programa {
  funcao inicio() {
    real peso, altura, imc

      escreva("Digite o peso: ")
      leia(peso)

      escreva("Digite a altura: ")
      leia(altura)

      imc = peso / (altura * altura)

      escreva("IMC: ", imc, "\n")

      se (imc < 18.5)
      {
          escreva("Magreza")
      }
      senao se (imc >= 18.5 e imc <= 24.9)
      {
          escreva("Normal")
      }
      senao se (imc >= 25 e imc <= 30)
      {
          escreva("Sobrepeso")
      }
      senao
      {
          escreva("Obesidade")
      }

  }
}
