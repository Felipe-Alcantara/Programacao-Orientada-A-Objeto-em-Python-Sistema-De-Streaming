class Cliente:
    def __init__(self, Nome, Email, Plano) -> None:
        self.Nome = Nome
        self.Email = Email
        self.Planos_disponíveis = ["Basic", "Premium"]
        self.Plano = Plano  # inicializar self.Plano aqui
        self.numero_Cliente = self.cliente_existente()
        if not self.plano_invalido():
            raise Exception("Erro de plano")
        if self.numero_Cliente is None:
            self.salvar_cliente()

    def __str__(self) -> str:
        return f"Cliente {self.numero_Cliente}: Nome: {self.Nome}\nEmail: {self.Email}\nPlano: {self.Plano}"

    
    def plano_invalido(self):  # remover o argumento Plano
        if self.Plano in self.Planos_disponíveis:
            return True
        else:
            return False
    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.Planos_disponíveis:
                self.Plano = novo_plano
                return True
        else:
            raise Exception("Erro de plano")


    def ver_filme(self, filme): #Neste caso "filme" significa o self da classe "Filme"
        if self.Plano == filme.planoNecessario:
            print(f"Filme: {filme.nomeFilme} disponível")
        elif self.Plano == "Premium":
            print(f"Filme: {filme.nomeFilme} disponível")
        elif self.Plano == "Basic" and filme.planoNecessario == "Premium":
            print(f"Filme: {filme.nomeFilme} para o usuário: {self.Nome} está: indisponível")

    def salvar_cliente(self):
        try:
            with open("Clientes.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1]
                    last_Cliente_num = int(last_line.split(":") [0].split()[-1])
                    self.numero_Cliente = last_Cliente_num + 1
                else:
                    self.numero_Cliente = 1
        except FileNotFoundError:
            self.numero_Cliente = 1
        
        with open("Clientes.txt", "a", encoding="utf-8") as f:
            f.write(f"Cliente {self.numero_Cliente}: {self.Nome}, Email: {self.Email}, Plano: {self.Plano}\n")

    def cliente_existente(self):
        try:
            with open("Clientes.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if self.Nome in line and self.Email in line and self.Plano in line:
                        return int(line.split(":")[0].split()[-1])
            return None
        except FileNotFoundError:
            return None