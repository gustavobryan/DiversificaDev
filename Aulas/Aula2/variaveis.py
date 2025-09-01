import datetime

# str - string(texto)
# type - tipo de dado
# int - inteiro (número inteiro)
# float - ponto flutuante (número com ponto decimal)
# bool - booleano (True/False)

nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "!")
ano_nascimento = input(nome + ", qual é o seu ano de nascimento? ")
print(nome + ", você nasceu em " + ano_nascimento + ".")
data_atual = datetime.date.today()
idade = data_atual.year - int(ano_nascimento)
print(nome + ", você tem " + str(idade) + " anos.")

resultado_jogo1 = 5
resultado_jogo2 = 3
resultado_jogo3 = -2
total_pontos = resultado_jogo1 + resultado_jogo2 + resultado_jogo3
print("Resultados dos jogos:")
print("Jogo 1: " + str(resultado_jogo1))
print("Jogo 2: " + str(resultado_jogo2))
print("Jogo 3: " + str(resultado_jogo3))
print("Total de pontos: " + str(total_pontos))
