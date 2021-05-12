import time


class CalcExecucao:

    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwds) -> str:
        inicio = time.time()
        self.func(*args, *kwds)
        final = time.time()

        return f"Tempo de execução de {self.func.__name__}: {(final - inicio)}"


if __name__ == "__main__":
    @CalcExecucao
    def teste(x, y):
        for c in range(x):
            if c % y == 0:
                print(c)


    print(teste(100, 2))