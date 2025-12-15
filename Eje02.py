class Biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[]
    
    def agregar_libro(self,libro):
        self.libros.append(libro)
    def listar_libros(self):
        for libro in self.libros:
            estado="Disponible" if libro.disponible else "No Disponible"
            print(f"{libro.titulo} por {libro.autor} ({libro.año}) - {estado}")
    def buscar_por_autor(self,autor):
        resultados=[libro for libro in self.libros if libro.autor==autor]
        return resultados   
    def prestar_libro(self,titulo):
        for libro in self.libros:
            if libro.titulo==titulo :
                libro.prestar()
                return True
        return False
class Libro:
    def __init__(self,titulo,autor,año,disponible):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.disponible=disponible
class libroFisico(Libro):
    def __init__(self,titulo,autor,año,paginas):
        super().__init__(titulo,autor,año,True)
        self.paginas=paginas
    def prestar(self):
        if self.disponible:
            print(f"Prestando libro físico: {self.titulo}")
            self.disponible=False
        else:
            print(f"El libro {self.titulo} no está disponible para préstamo.")
class libroDigital(Libro):
    def __init__(self,titulo,autor,año,tamano_mb):
        super().__init__(titulo,autor,año,True)
        self.tamano_mb=tamano_mb
    def prestar(self):
        if self.disponible:
            print(f"Prestando libro digital: {self.titulo}")
            self.disponible=False

biblioteca=Biblioteca("Biblioteca Central")
libro1=libroFisico("Cien Años de Soledad","Gabriel García Márquez",1967,417)
libro2=libroFisico("1984","George Orwell",1949,328)
libro3=libroFisico("Fahrenheit 451","Ray Bradbury",1953,194)
libro4=libroDigital("El Principito","Antoine de Saint-Exupéry",1943,1.5)
libro5=libroDigital("Don Quijote de la Mancha","Miguel de Cervantes",1605,3.2)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)
print("Listado de libros en la biblioteca:")
biblioteca.listar_libros()
print("\nPrestando '1984':")
if biblioteca.prestar_libro("1984"):
    print("Préstamo exitoso.")
else:
    print("El libro no está disponible.")
nveces=5
print("\nPrestndo 'El Principito':")
for _ in range(nveces):
    if biblioteca.prestar_libro("El Principito"):
        print("Préstamo exitoso.")
    else:
        print("El libro no está disponible.")

print("\nPrestar libro ya prestado '1984':")
if biblioteca.prestar_libro("1984"):
    print("Préstamo exitoso.")
else:
    print("El libro no esta disponible.")
print("\nBuscar libros por autor 'George Orwell':")
resultados=biblioteca.buscar_por_autor("George Orwell")
for libro in resultados:
    print(f"{libro.titulo} por {libro.autor} ({libro.año})")
