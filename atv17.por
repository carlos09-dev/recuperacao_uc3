programa {
  funcao inicio() {
     inteiro quantidade
        real preco, total

        escreva("Digite a quantidade de sucos: ")
        leia(quantidade)

        se (quantidade > 10)
        {
            preco = 4.50
        }
        senao
        {
            preco = 5.50
        }

        total = quantidade * preco

        escreva("Valor total a pagar: R$ ", total)
  }
}
