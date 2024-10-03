import suma
import random
import time
from fastapi import FastAPI
from math import sqrt

app = FastAPI()


def generar_lista_flotantes_aleatorios(tamano, minimo, maximo):
    """
    Genera una lista de números flotantes aleatorios.

    Parámetros:
    tamano (int): Número de elementos en la lista.
    minimo (float): Valor mínimo para los números aleatorios.
    maximo (float): Valor máximo para los números aleatorios.

    Retorna:
    list: Lista de números flotantes aleatorios.
    """
    return [random.uniform(minimo, maximo) for _ in range(tamano)]

COUNT = 500000000

def countdown(n):
    while n > 0:
        t = sqrt(n)
        n -= 1

def ejecutar():

    start = time.time()
    countdown(COUNT)
    end = time.time()

    var1 = 'Time taken in seconds: '
    var2 = end - start

    return '{var1}{var2}'.format(var1=var1, var2=var2)

def ejecutar2():

    start = time.time()
    resultado = suma.contador(COUNT)
    end = time.time()

    var1 = 'Time taken in seconds: '
    var2 = end - start

    return '{var1}{var2}, {var3}'.format(var1=var1, var2=var2, var3=resultado)

@app.get("/counter")
async def counterwcpp():
    
    str = ejecutar()
    return {"message": str}

@app.get("/counterwcpp")
async def counterwcpp():
    
    str = ejecutar2()
    return {"message": str}

@app.get("/navg")
async def sum_with_c():
    numbers = random.randint(5, 100)
    minimo = 1.0
    maximo = 1000.0

    numbers = generar_lista_flotantes_aleatorios(numbers, minimo, maximo)

    # Llamada a la función avg_floats
    result = suma.avg_floats(numbers)

    str=f"La media de {numbers} es: {result}"
    return {"message": str}


@app.get("/nsuma")
async def sum_with_c():
    # Lista aleatoria de números flotantes
    numbers = random.randint(5, 100)
    minimo = 1.0
    maximo = 1000.0

    numbers = generar_lista_flotantes_aleatorios(numbers, minimo, maximo)

    # Llamada a la función sum_floats
    result = suma.sum_floats(numbers)

    str=f"La suma de {numbers} es: {result}"
    return {"message": str}
 
