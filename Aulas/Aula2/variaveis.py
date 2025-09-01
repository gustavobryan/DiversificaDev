import datetime

nome = input("Qual é o seu nome? ")
print("Olá, " + nome + "!")
ano_nascimento = input(nome + ", qual é o seu ano de nascimento? ")
print(nome + ", você nasceu em " + ano_nascimento + ".")
data_atual = datetime.date.today()
idade = data_atual.year - int(ano_nascimento)
print(nome + ", você tem " + str(idade) + " anos.")