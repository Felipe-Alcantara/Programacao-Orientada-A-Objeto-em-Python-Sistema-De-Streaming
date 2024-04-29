class Filme:
    def __init__(self, nomeFilme, classificacao, planoNecessario) -> None:
        self.nomeFilme = nomeFilme
        self.classificacao = classificacao
        self.planoNecessario = planoNecessario
    
    def salvar_filme(self):
        try:
            with open("Filmes.txt", "r", encoding="utf-8") as f:
                for line in f:
                    nomeFilme, classificacao, planoNecessario = line.strip().split(", ")
                    if self.nomeFilme == nomeFilme:
                        print("Filme já existe")
                        return
        except FileNotFoundError as e:
            print(e)
            pass
        with open("Filmes.txt", "a", encoding="utf-8") as f:
            f.write(f"{self.nomeFilme}, {self.classificacao}, {self.planoNecessario}\n")
        print("Arquivo de filmes criado com sucesso.")  # Mensagem de confirmação após a escrita no arquivo