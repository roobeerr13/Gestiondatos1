class cliente:
    def __init__ (self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}, {self.nombre}, {self.apellido})"
    
class clientes:
    lista_clientes = []
    def buscar(dni):
        for cliente in clientes.lista_clientes:
            if cliente.dni == dni:
                return cliente