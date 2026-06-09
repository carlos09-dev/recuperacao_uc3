programa {
  funcao inicio() {
    cadeia nome
    real nota1,nota2, media,recuperacao

    escreva("digite o nome do aluno: ")
    leia(nome)

    escreva("digite nota1: ")
    leia(nota1)

    escreva("digite nota2: ")
    leia(nota2)

    media = (nota1 + nota2) / 2

    escreva("\nmedia: ", media, "\n")
    
    se (media >= 6.0)
    {
      escreva("APROVADO(A)")
    }
    senao
    {
      escreva("RECUPERACAO")
    }
      
    escreva("\n")
    escreva("digite nota da recuperacao: ")
    leia(recuperacao)

    se(recuperacao >= 5.0){
       escreva("APROVADA(O)!!")
    }
    senao{
       escreva("REPROVADA(O)")
    }
  }
}
