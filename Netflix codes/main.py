from Cliente import Cliente
from Filme import Filme

try:
    CriarCliente = Cliente("Felixo", "Felixo@Gmail.com", "Basic")
    print(CriarCliente.__str__())  # Aqui deve ser CriarCliente, não PrimeiroCliente
    print()
except Exception as e:
    print("Erro: ", e)

Filme_Premium = Filme("Filme teste", "Livre", "Premium")

# Testando acesso ao filme pelo plano
CriarCliente.ver_filme(Filme_Premium)
print()

# Botão upgrade:
CriarCliente.mudar_plano("Premium")
print(f"Seu plano atual agora é: {CriarCliente.Plano}")
print()

# Testando acesso ao filme pelo plano
CriarCliente.ver_filme(Filme_Premium)