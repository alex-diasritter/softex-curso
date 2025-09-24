from typing import List
from modulo2.desafios_poo.avançado.Livro import Livro

class Biblioteca:
    def __init__(self, acervo: List[Livro]):
        self.acervo = acervo

    def adicionar_livro(self, livro: Livro) -> None:
        self.acervo.append(livro)

    def listar_livros(self) -> None:
        for livro in self.acervo:
            print(livro.titulo, livro.autor)

biblioteca = Biblioteca([])

livro = Livro("java", "alexx")
livro2 = Livro("python", "anderson")
livro3 = Livro("java", "alexx")
livro4 = Livro("c++", "ricardo")

biblioteca.adicionar_livro(livro)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

biblioteca.listar_livros()


