# gestor/database.py
import csv
from . import config  # Cambiado de "import config" a "from . import config"

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

class Clientes:
    lista_clientes = []

    @classmethod
    def cargar(cls):
        cls.lista_clientes.clear()  # Limpiar la lista antes de cargar
        try:
            with open(config.DATABASE_PATH, newline="\n") as fichero:
                reader = csv.reader(fichero, delimiter=";")
                for dni, nombre, apellido in reader:
                    cliente = Cliente(dni, nombre, apellido)
                    cls.lista_clientes.append(cliente)
        except FileNotFoundError:
            cls.lista_clientes = []

    @classmethod
    def guardar(cls):
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for c in cls.lista_clientes:
                writer.writerow((c.dni, c.nombre, c.apellido))

    @classmethod
    def buscar(cls, dni):
        for cliente in cls.lista_clientes:
            if cliente.dni == dni:
                return cliente
        return None

    @classmethod
    def crear(cls, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        cls.lista_clientes.append(cliente)
        cls.guardar()
        return cliente

    @classmethod
    def modificar(cls, dni, nombre, apellido):
        for i, cliente in enumerate(cls.lista_clientes):
            if cliente.dni == dni:
                cls.lista_clientes[i].nombre = nombre
                cls.lista_clientes[i].apellido = apellido
                cls.guardar()
                return cls.lista_clientes[i]
        return None

    @classmethod
    def borrar(cls, dni):
        for i, cliente in enumerate(cls.lista_clientes):
            if cliente.dni == dni:
                cliente = cls.lista_clientes.pop(i)
                cls.guardar()
                return cliente
        return None

    def __init__(self):
        self.cargar()