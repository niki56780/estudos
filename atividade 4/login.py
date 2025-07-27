class Login:
    def login(self):
        self.usuario = input("Escolha seu usuário: ")
        self.senha = input("Digite sua senha: ")

    def verificar(self):
        usuario_input = input("Digite seu usuário, novamente: ")
        senha_input = input("Digite sua senha, novamente: ")
        if usuario_input == self.usuario and senha_input == self.senha:
            print("Deu certo seu login")
            return True
        else:
            print("Login falhou")
            return False
sistema = Login()
sistema.login()
sistema.verificar()
#unica maneira em que eu conseguiria fazer isso funcionar num reclame num
