# Procurar palavra -> Encontrar todas as ocorrências e indicar onde ocorrem
import os
import pathlib
import shutil
import zipfile


class ArquivoTexto:

    def __init__(self, arquivo_dir: str) -> None:
        self.arquivo_dir = pathlib.Path(arquivo_dir)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.arquivo_dir!r})"

    def __str__(self):
        return f"Diretório do arquivo a ser manipulado: {self.arquivo_dir}"

    def procurar_palavra(self, palavra: str) -> str:
        with open(self.arquivo_dir, encoding="utf8") as arquivo:
            contador = 0

            for linha in arquivo:
                contador += 1
                if palavra in linha:
                    return f"Encontrado: '{palavra}'. Linha: {contador}"

            return f"A palavra escolhida não aparece no arquivo inserido."

    def realocar_arquivo(self, caminho_novo: str) -> str:
        if os.path.isdir(caminho_novo):
            try:
                shutil.move(self.arquivo_dir, caminho_novo)
            except shutil.Error:
                return "Esse caminho já existe. Tente colocar outro."
            else:
                return f"Arquivo movido para {caminho_novo} com sucesso!"
        
        return "É preciso inserir um diretório válido."
            
    def renomear_arquivo(self, nome_novo: str) -> str:
        nome_novo = nome_novo + self.arquivo_dir.suffix
        dir_novo = os.path.join(os.path.dirname(self.arquivo_dir), nome_novo)
        os.rename(self.arquivo_dir, dir_novo)

        return f"{self.arquivo_dir} foi trocado para {dir_novo} com sucesso!"

    def zipar(self) -> str:
        nome_zip = self.arquivo_dir.stem + ".zip"

        with zipfile.ZipFile(nome_zip, "w") as arq_zip:
            arq_zip.write(self.arquivo_dir, arcname=self.arquivo_dir.name)
            return f"O arquivo '{nome_zip}' foi gerado com sucesso."
