import functools
import logging


def logger(func):
    logging.basicConfig(filename=f"logger", level=logging.INFO)

    @functools.wraps(func)
    def aninhada(*args, **kwargs):
        logging.info(f"'{func.__name__}' executado com os argumentos: {args}")
        return func(*args, **kwargs)

    return aninhada


def recibo(func):
    @functools.wraps(func)
    def aninhada(*args, **kwargs):

        with open("recibos.txt", "a") as arquivo:
            if func.__name__ == "depositar":
                arquivo.write(f"{args[0].nome} depositou R$ {args[1]}\n")
            elif func.__name__ == "sacar":
                arquivo.write(f"{args[0].nome} sacou R$ {args[1]}\n")
            else:
                arquivo.write(f"{args[0].nome} transferiu R$ {args[2]} para {args[1].nome}\n")

        return func(*args, **kwargs)

    return aninhada