import copy
import unittest
import csv
import config
import database as db
import helpers

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Configura la ruta del archivo CSV para pruebas
        config.DATABASE_PATH = 'gestor/tests/clientes_test.csv'

        # Crea un archivo CSV de prueba con datos iniciales
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            writer.writerow(['15J', 'Marta', 'Pérez'])
            writer.writerow(['48H', 'Manolo', 'López'])
            writer.writerow(['28Z', 'Ana', 'García'])

        # Inicializa la clase Clientes
        self.clientes = db.Clientes()

    def test_buscar_cliente(self):
        # Prueba buscar un cliente existente y uno no existente
        cliente_existente = self.clientes.buscar('15J')
        cliente_no_existente = self.clientes.buscar('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_no_existente)

    def test_crear_cliente(self):
        # Prueba crear un nuevo cliente
        nuevo_cliente = self.clientes.crear('39X', 'Héctor', 'Costa')
        self.assertEqual(len(self.clientes.lista_clientes), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')

    def test_modificar_cliente(self):
        # Prueba modificar un cliente existente
        cliente_a_modificar = copy.copy(self.clientes.buscar('28Z'))
        cliente_modificado = self.clientes.modificar('28Z', 'Mariana', 'Pérez')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        # Prueba borrar un cliente
        cliente_borrado = self.clientes.borrar('48H')
        cliente_rebuscado = self.clientes.buscar('48H')
        self.assertIsNone(cliente_rebuscado)
        self.assertEqual(cliente_borrado.dni, '48H')

    def test_escritura_csv(self):
        # Prueba que los cambios se reflejen en el archivo CSV
        self.clientes.borrar('48H')
        self.clientes.modificar('28Z', 'Mariana', 'Pérez')

        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            dni, nombre, apellido = next(reader)  # Primera línea del archivo

        self.assertEqual(dni, '15J')
        self.assertEqual(nombre, 'Marta')
        self.assertEqual(apellido, 'Pérez')

    def test_dni_valido(self):
        # Prueba la validación de DNIs
        self.assertTrue(helpers.leer_texto(3, 3, "00A"))
        self.assertFalse(helpers.leer_texto(3, 3, "23223S"))
        self.assertFalse(helpers.leer_texto(3, 3, "F35"))
        self.assertFalse(helpers.leer_texto(3, 3, "48H"))

if __name__ == '__main__':
    unittest.main()