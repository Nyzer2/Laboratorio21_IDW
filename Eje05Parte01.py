def copiar_texto(origen, destino):
    try:
        with open(origen, 'r') as archivo_origen:
            contenido = archivo_origen.read()
        with open(destino, 'w') as archivo_destino:
            archivo_destino.write(contenido)
        print(f"Contenido copiado de '{origen}' a '{destino}' exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

copiar_texto('archivo_origen.txt', 'archivo_destino.txt')