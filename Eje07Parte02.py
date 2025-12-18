import asyncio
import time
import random

async def consulta_db(id_consulta):
    tiempo = random.uniform(1, 5)
    await asyncio.sleep(tiempo) 
    print(f"Consulta {id_consulta} completada en {tiempo:.2f} segundos")
    return tiempo

async def main():
    inicio = time.time()
    tareas = [consulta_db(i) for i in range(1, 4)]
    await asyncio.gather(*tareas)  
    total = time.time() - inicio
    print(f"Tiempo total con asyncio: {total:.2f} segundos")

asyncio.run(main())