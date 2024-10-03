import suma
import random
import time
import asyncio
from fastapi import FastAPI, HTTPException
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

def countdown(n):
    while n > 0:
        t = sqrt(n)
        n -= 1

def ejecutar(number: int):

    start = time.time()
    countdown(number)
    end = time.time()

    var1 = 'Time taken in seconds: '
    var2 = end - start

    return '{var1}{var2}'.format(var1=var1, var2=var2)

def ejecutar2(number: int):

    start = time.time()
    resultado = suma.contador(number)
    end = time.time()

    var1 = 'Time taken in seconds: '
    var2 = end - start

    return '{var1}{var2}, {var3}'.format(var1=var1, var2=var2, var3=resultado)

@app.get("/counter")
async def long_task(number: int, timeout:float):
    async def counter(number):
        str = ejecutar(number)
        return {"message": str}

    try:
        result = await asyncio.wait_for(counter(number), timeout=timeout)
        return result
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Timeout en la operación interna")

@app.get("/counterwcpp")
async def counterwcpp(number: int):
    
    str = ejecutar2(number)
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
 
