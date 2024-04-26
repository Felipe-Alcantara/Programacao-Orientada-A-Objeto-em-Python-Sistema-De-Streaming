# Programacao-Orientada-A-Objeto-em-Python-Sistema-Netflix
 Este é um código Python que simula um sistema de streaming de filmes, semelhante ao Netflix. Ele define uma classe `Cliente` com atributos como `Nome`, `Email` e `Plano`. A classe inclui métodos para verificar a validade do plano, mudar o plano e verificar a disponibilidade de um filme com base no plano do cliente. O código também inclui um exemplo de como criar um objeto `Cliente` e como usar seus métodos.

# Sistema de Streaming de Filmes

Este é um código Python que simula um sistema de streaming de filmes, semelhante ao Netflix. 

## Classe Cliente

A classe `Cliente` é a principal classe do nosso sistema. Ela representa um cliente do serviço de streaming.

```python
class Cliente:
    def __init__(self, Nome, Email, Plano) -> None:
        self.Nome = Nome
        self.Email = Email
        self.Planos_disponíveis = ["Basic", "Premium"]
        if not self.plano_invalido(Plano):
            raise Exception("Erro de plano")
```

### Atributos

- `Nome`: Nome do cliente.
- `Email`: Email do cliente.
- `Planos_disponíveis`: Lista dos planos disponíveis para o cliente. Atualmente, temos dois planos: "Basic" e "Premium".
- `Plano`: Plano atual do cliente. É verificado se o plano é válido no momento da criação do cliente.

### Métodos

- `plano_invalido(self, Plano)`: Verifica se o plano indicado para o cliente é válido. Se for inválido, o cliente não é criado e um erro é lançado.
- `mudar_plano(self, novo_plano)`: Permite ao cliente mudar de plano. Se o novo plano for inválido, um erro é lançado.
- `ver_filme(self, filme, Plano_Filme)`: Verifica se um filme está disponível para o cliente, com base no plano do cliente.

## Exemplo de Uso

```python
try:
    PrimeiroCliente = Cliente("Felipe", "Felipe@Gmail.com", "Basic")
    print(PrimeiroCliente.__str__())
except Exception as e:
    print("Erro: ", e) 

PrimeiroCliente.mudar_plano("Basic")
print(f"Seu plano atual agora é: {PrimeiroCliente.Plano}")

PrimeiroCliente.ver_filme("Filme", "Premium")
```

Neste exemplo, criamos um cliente chamado Felipe com o plano "Basic". Em seguida, tentamos mudar o plano para "Basic" novamente e verificamos a disponibilidade de um filme "Premium" para ele.