import csv
import config  # Importar la configuración

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}, {self.nombre}, {self.apellido})"

class Clientes:
    def __init__(self):
        self.lista_clientes = []
        with open(config.DATABASE_PATH, newline="\n") as fichero:  # Usar DATABASE_PATH
            reader = csv.reader(fichero, delimiter=";")
            for dni, nombre, apellido in reader:
                cliente = Cliente(dni, nombre, apellido)
                self.lista_clientes.append(cliente)

    def guardar(self):
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:  # Usar DATABASE_PATH
            writer = csv.writer(fichero, delimiter=";")
            for c in self.lista_clientes:
                writer.writerow((c.dni, c.nombre, c.apellido))

    def buscar(self, dni):
        for cliente in self.lista_clientes:
            if cliente.dni == dni:
                return cliente

    def crear(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.lista_clientes.append(cliente)
        self.guardar()
        return cliente

    def modificar(self, dni, nombre, apellido):
        for i, cliente in enumerate(self.lista_clientes):
            if cliente.dni == dni:
                self.lista_clientes[i].nombre = nombre
                self.lista_clientes[i].apellido = apellido
                self.guardar()
                return self.lista_clientes[i]

    def borrar(self, dni):
        for i, cliente in enumerate(self.lista_clientes):
            if cliente.dni == dni:
                cliente = self.lista_clientes.pop(i)
                self.guardar()
                return cliente