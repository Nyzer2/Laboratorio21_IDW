import threading
import time
import random

def consulta_db(id_consulta):
    tiempo = random.uniform(1, 5)
    time.sleep(tiempo)
    print(f"Consulta {id_consulta} completada en {tiempo:.2f} segundos")
    return tiempo

inicio = time.time()
hilos = []
resultados = []

def ejecutar_consulta(id_consulta):
    resultados.append(consulta_db(id_consulta))

for i in range(1, 4):
    hilo = threading.Thread(target=ejecutar_consulta, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

total = time.time() - inicio
print(f"Tiempo total con hilos: {total:.2f} segundos")