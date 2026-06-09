programa {
  funcao inicio() {
    real gasolina, etanol, resultado

    escreva("Digite o preço da gasolina: ")
    leia(gasolina)

    escreva("Digite o preço do etanol: ")
    leia(etanol)

    resultado = etanol / gasolina

    se (resultado >= 0.7)
    {
      escreva("Vale apena abastecer com gasolina.")
    }
    senao
    {
      escreva("Vale apena abastecer com etanol.")
    }
  }
}
