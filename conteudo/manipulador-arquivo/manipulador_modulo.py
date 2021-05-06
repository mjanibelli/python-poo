# Procurar palavra -> Encontrar todas as ocorrências e indicar onde ocorrem
# Zipar
# Realocar arquivo

import os
import pathlib


class ArquivoTexto:

    def __init__(self, arquivo_dir):
        self.arquivo_dir = pathlib.Path(arquivo_dir)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.arquivo_dir!r})"

    def __str__(self):
        return f"Diretório do arquivo a ser manipulado: {self.arquivo_dir}"

    def procurar_palavra(self, palavra):
        with open(self.arquivo_dir, encoding="utf8") as arquivo:
            contador = 0

            for linha in arquivo:
                contador += 1
                if palavra in linha:
                    return f"Palavra '{palavra}' encontrada. Linha: {contador}"

            return f"A palavra que escolheu não aparece no arquivo inserido."
            
    def renomear_arquivo(self, nome_novo):
        nome_novo = nome_novo + self.arquivo_dir.suffix
        dir_novo = os.path.join(os.path.dirname(self.arquivo_dir), nome_novo)
        os.rename(self.arquivo_dir, dir_novo)

        return f"{self.arquivo_dir} foi trocado para {dir_novo} com sucesso!"
