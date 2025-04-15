# gestor/database.py
import csv

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

class Clientes:
    # Ruta del archivo, configurable
    archivo = "clientes.csv"  # Ajusta esta ruta si el archivo está en otro lugar
    
    # Lista de clientes
    lista = []

    @classmethod
    def cargar(cls):
        cls.lista.clear()  # Limpiar la lista antes de cargar
        try:
            with open(cls.archivo, newline="\n") as fichero:
                reader = csv.reader(fichero, delimiter=";")
                for dni, nombre, apellido in reader:
                    cliente = Cliente(dni, nombre, apellido)
                    cls.lista.append(cliente)
        except FileNotFoundError:
            # Si el archivo no existe, inicializamos una lista vacía
            cls.lista = []

    @classmethod
    def guardar(cls):
        with open(cls.archivo, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for c in cls.lista:
                writer.writerow((c.dni, c.nombre, c.apellido))

    @classmethod
    def crear(cls, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        cls.lista.append(cliente)
        cls.guardar()
        return cliente

    @classmethod
    def modificar(cls, dni, nombre, apellido):
        for i, cliente in enumerate(cls.lista):
            if cliente.dni == dni:
                cls.lista[i].nombre = nombre
                cls.lista[i].apellido = apellido
                cls.guardar()
                return cls.lista[i]
        return None

    @classmethod
    def borrar(cls, dni):
        for i, cliente in enumerate(cls.lista):
            if cliente.dni == dni:
                cliente = cls.lista.pop(i)
                cls.guardar()
                return cliente
        return None