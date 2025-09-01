# Operações: soma
def soma(a, b):
    return a + b
print("Soma:", soma(5, 3))

# Operações: subtração
def subtracao(a, b):
    return a - b
print("Subtração:", subtracao(5, 3))

# Operações: multiplicação
def multiplicacao(a, b):
    return a * b
print("Multiplicação:", multiplicacao(5, 3))

# Operações: divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."
print("Divisão:", divisao(5, 0))

# Operações: potência
def potencia(a, b):
    return a ** b
print("Potência:", potencia(5, 3))

# Operações: radiciação
def radiciacao(a, b):
    return a ** (1 / b)

print("Radiciação:", radiciacao(25, 2))

# Operações: módulo/ resto da divisão
def modulo(a, b):
    return a % b
print("Módulo:", modulo(5, 3))

# Operações Lógicas: true / false
def logica_verdadeira():
    return 10 >= 3 

def logica_falsa():
    return 3 >= 10

print("Lógica Verdadeira:", logica_verdadeira())
print("Lógica Falsa:", logica_falsa())

n1 = 100
teste_logico = n1 % 2 == 0
print(teste_logico)

# --- IGNORE --- in

frase = "O rato roeu a roupa do rei de Roma."
palavra = "rei"
print(palavra in frase)