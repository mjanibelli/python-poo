import datetime
import logging
import time


class LoggerDecorator:

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        logging.basicConfig(filename=f"logger.log", level=logging.INFO)
        hora = datetime.datetime.now().strftime("%H:%M")
        tempo_ini = time.time()

        self.func(*args, **kwargs)

        tempo_final = time.time()
        tempo_exec = (tempo_final - tempo_ini)
        logging.info(
            f"Exec:{self.func.__name__}{args}{kwargs} Tempo:{tempo_exec} [{hora}]")


if __name__ == "__main__":

    @LoggerDecorator
    def teste(num1, num2, limite):
        for x in range(limite):
            print((num1+num2) ** x)

    
teste(1, 1, 1000)
