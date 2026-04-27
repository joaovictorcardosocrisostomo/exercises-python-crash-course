from user import User
#9.8
class Privileges():
  def __init__(self, privilegios):
    self.privileges = privilegios
  
  def show_privileges(self):
    for privilege in self.privileges:
      print(privilege)

class Admin(User):
  """Modelando um admin"""
  def __init__(self, first_name, last_name, *privileges, **user_info):
    #o *privileges vai capturar todos os argumentos posicionais extras e 
    #transformá-los em uma tupla, enquanto o **user_info capturará os argumentos
    #nomeados e os transformará em um dicionário.
      super().__init__(first_name, last_name, **user_info)
      self.privilegios = Privileges(privileges)