from io import FileIO
import os
import pathlib
import shutil
import zipfile

from PyPDF2 import PdfFileReader, PdfFileWriter


class ArquivoTexto:

    def __init__(self, arquivo_dir: str) -> None:
        self.arquivo_dir = pathlib.Path(arquivo_dir)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.arquivo_dir!r})"

    def __str__(self) -> str:
        return f"Diretório do arquivo a ser manipulado: {self.arquivo_dir}"

    def gerarsenha_pdf(self, senha: str) -> str:
        if self.arquivo_dir.suffix == ".pdf":
            escritor = PdfFileWriter()
            pdf = PdfFileReader(FileIO(self.arquivo_dir.absolute(), "rb"))

            for pagina in range(pdf.numPages):
                escritor.addPage(pdf.getPage(pagina))
            escritor.encrypt(senha)

            with open(f"senha_{self.arquivo_dir.name}", "wb") as arquivo:
                escritor.write(arquivo)

            return f"'senha_{self.arquivo_dir.name}' foi criado com sucesso!" 
        
        else:
            return "O arquivo precisa ser um PDF."


    def procurar_palavra(self, palavra: str) -> str:
        with open(self.arquivo_dir, encoding="utf8") as arquivo:
            contador = 0
            linhas = []

            for linha in arquivo:
                contador += 1

                if palavra in linha:
                    linhas.append(contador)
                    continue
                
            if linhas:
                return f"'{palavra}' aparece nas seguintes linhas: {linhas}"

            return f"A palavra escolhida não aparece no arquivo inserido."

    def realocar_arquivo(self, caminho_novo: str) -> str:
        if os.path.isdir(caminho_novo):
            try:
                novo_local = shutil.move(self.arquivo_dir, caminho_novo)
            except shutil.Error:
                return "Esse caminho já existe. Tente colocar outro."
            else:
                self.arquivo_dir = pathlib.Path(novo_local)
                return f"Arquivo movido para {caminho_novo} com sucesso!"
        
        return "É preciso inserir um diretório válido."
            
    def renomear_arquivo(self, nome_novo: str) -> str:
        nome_novo = nome_novo + self.arquivo_dir.suffix
        dir_novo = os.path.join(os.path.dirname(self.arquivo_dir), nome_novo)
        os.rename(self.arquivo_dir, dir_novo)
        self.arquivo_dir = pathlib.Path(dir_novo)

        return f"{self.arquivo_dir} foi trocado para {dir_novo} com sucesso!"

    def zipar(self) -> str:
        nome_zip = self.arquivo_dir.stem + ".zip"

        with zipfile.ZipFile(nome_zip, "w") as arq_zip:
            arq_zip.write(self.arquivo_dir, arcname=self.arquivo_dir.name)
            return f"O arquivo '{nome_zip}' foi gerado com sucesso."
