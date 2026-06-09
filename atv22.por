programa {
  funcao inicio() {
cadeia letra

  escreva("Digite a letra do suco (L, M, A ou U): ")
  leia(letra)

  se (letra == "L" ou letra == "l")
  {
      escreva("Suco de Laranja - Vitamina C")
  }
  senao se (letra == "M" ou letra == "m")
  {
      escreva("Suco de Morango - Vitamina A")
  }
  senao se (letra == "A" ou letra == "a")
  {
      escreva("Suco de Acerola - Vitamina C")
  }
  senao se (letra == "U" ou letra == "u")
  {
      escreva("Suco de Uva - Vitamina E")
  }
  senao
  {
      escreva("Opcao invalida!")
  }  
  }
}
