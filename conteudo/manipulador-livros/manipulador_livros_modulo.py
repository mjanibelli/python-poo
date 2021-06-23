"""Programa que vai utilizar Web Scrapping para auxiliar na busca
de livros e de resumos.
"""


class Livro:

    def __init__(self, nome, autor=""):
        self.nome = nome.title()
        self.autor = autor.title()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.nome!r}, {self.autor!r})"

    def __str__(self) -> str:
        return f"O livro escolhido é o: {self.nome}, escrito por {self.autor}"

    def procurar_livro(self):
        """Verifica se um livro está disponível no domínio público.
        Se sim, retorna um link para acessá-lo.
        """
        pass

    def resumo_livro(self):
        """Procura por um resumo do livro escolhido no site
        'https://educacao.uol.com.br/resumos-de-livros/'.
        Caso haja um resumo, retorna um link para acessá-lo."""
        pass
