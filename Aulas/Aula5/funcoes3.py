import random
def cadastrar_usuario():
    nome = input('Insira seu nome: ')
    idade = input('Insira sua idade: ')
    cep = input('Insira seu CEP: ')
    data_nascimento = input('Insira sua data de nascimento: ')
    usuario = {'nome': nome, 'idade': idade, 'cep': cep, 'data_nascimento': data_nascimento}
    return usuario

usuarios = []
continuar = True

for i in range(50):
  print(random.randint(1, 100))  # Apenas para ilustrar o uso do import random
  """
  usuario = cadastrar_usuario()
  usuarios.append(usuario)
  print(usuario)

  print('Usuário cadastrado com sucesso!')
  resposta = input('Deseja cadastrar outro usuário? (s/n): ')

  if resposta.lower() != 's':
      continuar = False
      print('Lista de usuários cadastrados:', usuarios)"""