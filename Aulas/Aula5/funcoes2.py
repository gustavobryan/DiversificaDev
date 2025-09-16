continuar = True
while continuar:
    n = input("Insira um número: ")
    n = int(n)
    print(n ** 2)
    resposta = input("Deseja continuar? (s/n): ")
if resposta.lower() != "s":
    continuar = False