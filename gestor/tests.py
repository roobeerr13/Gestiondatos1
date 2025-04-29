# gestor/tests.py
import copy
import unittest
import csv
import os
import gestor.config as config  # Cambiado a importación absoluta
import gestor.database as db    # Cambiado a importación absoluta
import gestor.helpers as helpers  # Cambiado a importación absoluta

class TestDatabase(unittest.TestCase):
    def setUp(self):
        config.DATABASE_PATH = 'gestor/tests/clientes_test.csv'

        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            writer.writerow(['15J', 'Marta', 'Pérez'])
            writer.writerow(['48H', 'Manolo', 'López'])
            writer.writerow(['28Z', 'Ana', 'García'])

        self.clientes = db.Clientes()

    def tearDown(self):
        # Limpiar el archivo temporal después de cada test
        if os.path.exists(config.DATABASE_PATH):
            os.remove(config.DATABASE_PATH)
        # Limpiar la lista de clientes para evitar interferencias
        self.clientes.lista_clientes.clear()

    def test_buscar_cliente(self):
        # Prueba buscar un cliente existente y uno no existente
        cliente_existente = self.clientes.buscar('15J')
        cliente_no_existente = self.clientes.buscar('99X')
        self.assertIsNotNone(cliente_existente)
        self.assertEqual(cliente_existente.dni, '15J')
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
        self.assertEqual(cliente_a_modificar.apellido, 'García')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')
        self.assertEqual(cliente_modificado.apellido, 'Pérez')

    def test_borrar_cliente(self):
        # Prueba borrar un cliente
        cliente_borrado = self.clientes.borrar('48H')
        cliente_rebuscado = self.clientes.buscar('48H')
        self.assertIsNone(cliente_rebuscado)
        self.assertEqual(cliente_borrado.dni, '48H')

    def test_escritura_csv(self):
        self.clientes.borrar('48H')
        self.clientes.modificar('28Z', 'Mariana', 'Pérez')
        self.clientes.crear('39X', 'Héctor', 'Costa')

        # Leer el archivo y verificar su contenido completo
        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            datos = list(reader)

        # Verificar que el archivo contiene exactamente lo esperado
        expected = [
            ['15J', 'Marta', 'Pérez'],
            ['28Z', 'Mariana', 'Pérez'],
            ['39X', 'Héctor', 'Costa']
        ]
        self.assertEqual(datos, expected)

    def test_dni_valido(self):
        self.assertTrue(helpers.leer_texto(3, 3, "00A"))
        self.assertFalse(helpers.leer_texto(3, 3, "23223S"))
        self.assertFalse(helpers.leer_texto(3, 3, "F35"))
        self.assertFalse(helpers.leer_texto(3, 3, "48H"))


if __name__ == '__main__':
    unittest.main()