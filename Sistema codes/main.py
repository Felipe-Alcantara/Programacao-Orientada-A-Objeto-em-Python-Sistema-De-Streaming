from Cliente import Cliente
from Filme import Filme

try:
    cliente = Cliente("batatatata", "Felixo@Gmail.com", "Basic", 18)
    print(cliente.__str__())  # Aqui deve ser cliente, não PrimeiroCliente
    print()
except Exception as e:
    print("Erro: ", e)

filme = Filme("Filme teste", 10, "Basic")

resultado = cliente.verificar(filme)
print(resultado)

if resultado == True:
    print("Disponível")
else:
    print("indisponível")

# # Testando acesso ao filme pelo plano
# resultado = cliente.verificar_plano(Filme_Premium)
# print(resultado)

# # Botão upgrade:
# cliente.mudar_plano("Premium")
# print(f"Seu plano atual agora é: {cliente.Plano}")
# print()

# # Testando acesso ao filme pelo plano
# resultado = cliente.verificar_plano(Filme_Premium)
# print(resultado)
# # Testando acesso ao filme pelo plano
# cliente.ver_filme(Filme_Premium)