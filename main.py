import math

def f(x):
    return x**2 - 2

def bissecao(a, b, e):
    if f(a) * f(b) >= 0:
        print("Não há raiz no intervalo")
        return None
    while (b - a) / 2 > e:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
e = float(input("Digite o valor de e: "))
print("A raiz é: ", bissecao(a, b, e))

