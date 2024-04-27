# Vamos criar um exemplo usando a Netflix

class Cliente:
    numero_Cliente = 0

    def __init__(self, Nome, Email, Plano) -> None:
        self.Nome = Nome
        self.Email = Email
        self.Planos_disponíveis = ["Basic", "Premium"]
        if not self.plano_invalido(Plano):
            raise Exception("Erro de plano")
        if not self.cliente_existente():
            self.salvar_cliente()

    def __str__(self) -> str:
        return f"Cliente {self.numero_Cliente}: Nome: {self.Nome}\nEmail: {self.Email}\nPlano: {self.Plano}"

    
    def plano_invalido(self, Plano): #Essa função verifica se o plano indicado para o cliente é valido, caso contrário, o cliente não é criado ("Erro de plano")
        if Plano in self.Planos_disponíveis:
            self.Plano = Plano
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
                        return True
            return False
        except FileNotFoundError:
            return False


class Filme:
    def __init__(self, nomeFilme, classificacao, planoNecessario) -> None:
        self.nomeFilme = nomeFilme
        self.classificacao = classificacao
        self.planoNecessario = planoNecessario

try:
    PrimeiroCliente = Cliente("Felipe", "Felipe@Gmail.com", "Basic")
    print(PrimeiroCliente.__str__())
    print()
# Cliente.add_to_database #Para adicionar as informações ao banco de dados
except Exception as e:
    print("Erro: ", e) 

try:
    SegundoCliente = Cliente("Júlio", "Júlio@Gmail.com", "Premium")
    print(SegundoCliente.__str__())
    print()
except Exception as e:
    print("Erro: ", e) 

Filme_Premium = Filme("Filme teste", "Livre", "Premium")
print()

# Testando acesso ao filme pelo plano
PrimeiroCliente.ver_filme(Filme_Premium)
print()

# Botão upgrade:
PrimeiroCliente.mudar_plano("Premium")
print(f"Seu plano atual agora é: {PrimeiroCliente.Plano}")
print()

# Testando acesso ao filme pelo plano
PrimeiroCliente.ver_filme(Filme_Premium)