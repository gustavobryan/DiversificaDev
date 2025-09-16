usuarios = []
continuar = True
while continuar:
  nome = input('Insira seu nome: '),
  idade = input('Insira sua idade: ')
  cep = input('Insira seu CEP: ')
  email = input('Insira seu email: ')
  data_nascimento = input('Insira sua data de nascimento: ')

  usuario = {'nome': nome, 'idade': idade, 'cep': cep, 'email': email, 'data_nascimento': data_nascimento}
  usuarios.append(usuario)
  print(usuario)

  print('Usuário cadastrado com sucesso!')
  resposta = input('Deseja cadastrar outro usuário? (s/n): ')

  if resposta.lower() != 's':
      continuar = False
print('Lista de usuários cadastrados:', usuarios)
