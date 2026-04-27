class User():
    def __init__(self, first_name, last_name, **user_info):
        #passar user info aqui é uma boa solução quando você tem informações
        #padronizadas em um formulário, mas nem todas são obrigatórias
        """modela um usuário genérico"""
        self.profile = {}
        """recebe informações adicionaisque podem ou não existir."""
        self.profile['name'] = str(first_name) + " " + str(last_name)
        """nome completo do usuário. é mais adequado guardar separado."""

        for key, value in user_info.items():
            """separa os dados que vieram no dicionário passado no argumento"""
            self.profile[key] = value
            
    def greet_user(self):
        """saudação simples"""
        print(f"Olá, {self.profile['name'].title()}!")

    def describe_user(self):
        """apresenta os dados do usuário"""
        print(f"Dados do user {self.profile['name'].title()}:")
        for key, value in self.profile.items():
            if key == 'name':
                print(f"{key.title()}: {value}")
            else:
             print(f"{key}: {value}")
