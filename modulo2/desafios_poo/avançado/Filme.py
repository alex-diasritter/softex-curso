class Filme:
    def __init__(self, nome: str, diretor: str):
        self.nome = nome
        self.diretor = diretor

    def __str__(self) -> str:
        return f"Filme: '{self.nome}' - Diretor: {self.diretor}"

filme = Filme("De volta pro futuro", "Steven Spielberg")

# caso o metodo __str__ nao seja sobrescrito o retorno é o endereco de memoria do objeto
print(filme)