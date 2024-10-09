import time

def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio