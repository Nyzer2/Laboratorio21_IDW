import multiprocessing
import time
import random

def consulta_db(id_consulta):
    tiempo = random.uniform(1, 5)
    time.sleep(tiempo)
    print(f"Consulta {id_consulta} completada en {tiempo:.2f} segundos")
    return tiempo

if __name__ == "__main__":  
    inicio = time.time()
    with multiprocessing.Pool(processes=3) as pool:
        resultados = pool.map(consulta_db, range(1, 4))
    total = time.time() - inicio
    print(f"Tiempo total con procesos: {total:.2f} segundos")