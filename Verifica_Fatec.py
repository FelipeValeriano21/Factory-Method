from abc import ABC, abstractmethod 


class Fatec(ABC):
 @abstractmethod
 def apresentar(self, nome):
  pass



# Subclasse de FATEC
class Aluno(Fatec):
 def apresentar(self, nome,relacao_pessoa):
    return f"{nome} tem relação com a instituição como {relacao_pessoa}"


# Subclasse de FATEC
class Professor(Fatec):
 def apresentar(self,nome, relacao_pessoa):
    return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
# Subclasse de FATEC
class Cordenador(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
 # Subclasse de FATEC
class Diretor(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
 # Subclasse de FATEC
class Administrativo(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"
 
 # Subclasse de FATEC
class Vestibulando(Fatec):
 def apresentar(self, nome, relacao_pessoa):
      return f"{nome} tem relação com a instituição como {relacao_pessoa}"



# Classe Factory Method
class CriaPortaria:
 
 def Criar_Chamada(self, opcao):
   
  if opcao == "Aluno":
   return Aluno()
  elif opcao == "Professor":
   return Professor()
  elif opcao == "Cordenador":
   return Cordenador() 
  elif opcao == "Diretor":
    return Diretor()
  elif opcao == "Administrativo": 
    return Administrativo()
  elif opcao == "Vestibulando":
    return Vestibulando()
  else:
   raise ValueError("Tipo de usuario não encontrado")
  




# Menu com a escolha de relação

def menu_loop():

   print ("Bem-vindo ao sistema da Fatec\n")


   op = input("Digite qualquer tecla para iniciar e Q para Sair\n")


   while op != "Q":   

      Cria_Portaria = CriaPortaria()
      nome = input ("Entre com o seu nome:\n")
      relacao_pessoa = input ("Qual a sua relação com a FATEC:\n")
      usuario = Cria_Portaria.Criar_Chamada(relacao_pessoa)   
      print(usuario.apresentar(nome, relacao_pessoa))

      print("\n\n\n\n")


menu_loop()











