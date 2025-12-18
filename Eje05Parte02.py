def copiar_binario(origen, destino):
    try:
        with open(origen, 'rb') as archivo_origen:
            with open(destino, 'wb') as archivo_destino:
                while True:
                    bloque = archivo_origen.read(1024)  
                    if not bloque:
                        break
                    archivo_destino.write(bloque)
        print(f"Contenido copiado de '{origen}' a '{destino}' exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

copiar_binario('imagen_origen.jpg', 'imagen_destino.jpg')