programa {
  funcao inicio() {
     cadeia item1, item2

        escreva("Digite o primeiro item: ")
        leia(item1)

        escreva("Digite o segundo item: ")
        leia(item2)

        se ((item1 == "10paes" e item2 == "queijo") ou (item1 == "queijo" e item2 == "10paes"))
        {
            escreva("Desconto de 10%")
        }
        senao se (item1 == "bisnaga" ou item1 == "pao_de_forma" ou item2 == "bisnaga" ou item2 == "pao_de_forma")
        {
            escreva("Desconto de 15%")
        }
        senao se ((item1 == "leite" e (item2 == "pao_doce" ou item2 == "suspiro")) ou
                  (item2 == "leite" e (item1 == "pao_doce" ou item1 == "suspiro")))
        {
            escreva("Desconto de 5%")
        }
        senao
        {
            escreva("Sem desconto")
        }
  }
}
