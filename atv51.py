def soma(a, b):
    resultado = a + b
    print("Soma =", resultado)
    return resultado

def subtracao(a, b):
    resultado = a - b
    print("Subtração =", resultado)
    return resultado

def multiplicacao(a, b):
    resultado = a * b
    print("Multiplicação =", resultado)
    return resultado

def divisao(a, b):
    resultado = a / b
    print("Divisão =", resultado)
    return resultado

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

r1 = soma(n1, n2)
r2 = subtracao(n1, n2)
r3 = multiplicacao(n1, n2)
r4 = divisao(n1, n2)

print("Soma dos retornos =", r1 + r2 + r3 + r4)