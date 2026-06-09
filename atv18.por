programa {
  funcao inicio() {
    cadeia resposta

    escreva("Precisa de atendimento prioritário? (sim/nao): ")
    leia(resposta)

    se (resposta == "sim")
    {
      escreva("Vá para os caixas 1, 2 e 3.")
    }
    senao
    {
       escreva("Vá para qualquer caixa, exceto os 1, 2 e 3, que são prioritários.")
   }
  }
}
