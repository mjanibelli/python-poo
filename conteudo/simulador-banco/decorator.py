import logging


def logger(func):
    logging.basicConfig(filename=f"logger", level=logging.INFO)

    def aninhada(*args, **kwargs):
        logging.info(f"'{func.__name__}' executado com os argumentos: {args}")
        return func(*args, **kwargs)

    return aninhada