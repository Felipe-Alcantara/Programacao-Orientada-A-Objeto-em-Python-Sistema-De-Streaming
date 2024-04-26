# Programacao-Orientada-A-Objeto-em-Python-Sistema-Netflix
 Este é um código Python que simula um sistema de streaming de filmes, semelhante ao Netflix. Ele define uma classe `Cliente` com atributos como `Nome`, `Email` e `Plano`. A classe inclui métodos para verificar a validade do plano, mudar o plano e verificar a disponibilidade de um filme com base no plano do cliente. O código também inclui um exemplo de como criar um objeto `Cliente` e como usar seus métodos.

# Sistema de Streaming de Filmes

Este código está relacionado à criação e manipulação de um objeto `Cliente` que representa um cliente da Netflix. Ele define uma classe chamada `Cliente` com métodos para criar um cliente, mudar o plano de assinatura do cliente e verificar se um filme está disponível para o cliente com base em seu plano de assinatura. O código instancia um objeto dessa classe e realiza operações nele. Em resumo, este código trabalha para modelar um cliente da Netflix e suas operações.

**Descrição do Projeto**

Este projeto consiste em um sistema simples de gerenciamento de clientes da Netflix. O projeto é composto por um único arquivo:

1. `Cliente.py`
Este arquivo contém a definição de uma classe Python chamada `Cliente`. A classe `Cliente` possui os seguintes métodos:

- `__init__(self, Nome, Email, Plano)`: Este método inicializa um objeto `Cliente` com um nome, email e plano de assinatura específicos. Se o plano de assinatura não for válido, uma exceção é lançada.

- `__str__(self)`: Este método retorna uma representação em string do objeto `Cliente`.

- `plano_invalido(self, Plano)`: Este método verifica se o plano de assinatura fornecido é válido.

- `mudar_plano(self, novo_plano)`: Este método muda o plano de assinatura do cliente para um novo plano. Se o novo plano não for válido, uma exceção é lançada.

- `ver_filme(self, filme, Plano_Filme)`: Este método verifica se um filme está disponível para o cliente com base em seu plano de assinatura.

O código realiza as seguintes operações:

- Instancia um objeto da classe `Cliente`, atribui atributos específicos a ele e imprime a representação em string do cliente.

- Chama o método `mudar_plano` no cliente para mudar o plano de assinatura.

- Chama o método `ver_filme` no cliente para verificar se um filme está disponível para o cliente com base em seu plano de assinatura.

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

Este projeto pode ser útil em várias situações, especialmente para desenvolvedores que desejam entender a programação orientada a objetos em Python e como ela pode ser usada para modelar situações do mundo real. Algumas maneiras pelas quais esse projeto pode ser útil incluem:

- **Aprendizado de POO**: Permite aos desenvolvedores aprenderem sobre classes, objetos e métodos em Python.

- **Modelagem de Objetos do Mundo Real**: Ajuda a entender como os objetos do mundo real, como clientes de um serviço de streaming, podem ser modelados em código.

- **Base para Projetos Mais Complexos**: Serve como uma base para projetos mais complexos que envolvem a interação com APIs de serviços de streaming.

Este projeto pode ajudar os desenvolvedores a entender melhor a programação orientada a objetos em Python, melhorar suas habilidades de codificação e criar projetos mais complexos.