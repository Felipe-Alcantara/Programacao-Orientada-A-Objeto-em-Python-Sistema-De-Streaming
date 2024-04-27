# Programação Orientada a Objetos em Python - Sistema Netflix

Este repositório contém um projeto simples que simula algumas funcionalidades do sistema Netflix. O projeto é escrito em Python e utiliza o paradigma de Programação Orientada a Objetos (POO).

## Arquivos

O projeto é composto por três arquivos principais:

1. `Cliente.py`: Este arquivo define a classe `Cliente`, que representa um cliente da Netflix. Cada cliente tem um nome, email e plano de assinatura.

2. `Filme.py`: Este arquivo define a classe `Filme`, que representa um filme disponível na Netflix. Cada filme tem um nome, classificação etária e plano necessário para acessá-lo.

3. `main.py`: Este é o arquivo principal que utiliza as classes `Cliente` e `Filme` para simular a interação de um cliente com o sistema Netflix.

## Funcionalidades

### Classe Cliente

A classe `Cliente` possui várias funcionalidades:

- **Inicialização**: Ao criar um novo cliente, é necessário fornecer um nome, email e plano de assinatura. Se o plano fornecido não for válido, uma exceção será lançada.

- **Mudança de plano**: Um cliente pode mudar seu plano de assinatura a qualquer momento.

- **Visualização de filmes**: Um cliente pode tentar assistir a um filme. Se o plano de assinatura do cliente for compatível com o plano necessário do filme, o filme estará disponível para visualização.

- **Salvamento de clientes**: Quando um novo cliente é criado, seus detalhes são salvos em um arquivo chamado `Clientes.txt`.

### Classe Filme

A classe `Filme` é mais simples e apenas contém informações sobre um filme.

## Utilidade

Este projeto pode ser útil para entender os conceitos básicos de POO em Python. Ele mostra como definir classes, criar objetos, usar métodos e interagir com arquivos. Embora seja um projeto simples, ele pode ser expandido com novas funcionalidades para torná-lo mais complexo e interessante.