import copy
import unittest
import database as db


class TestDatabase (unittest.TestCase):
    def setUp(self):
        db.clientes.lista_clientes = [
            db.cliente("12345678A", "Juan", "Pérez"),
            db.cliente("87654321B", "Ana", "Gómez"),
            db.cliente("11223344C", "Luis", "Martínez")
        ]

    def test_buscar_cliente(self):
        cliente_existente= db.clientes.crear('39X', 'Héctor', 'Costa')
        self .assertEqual(len(db.clientes.lista_clientes), 4)
        self.assertEqual(nuevo_cliente.dni, '39X')
        self.assertEqual(nuevo_cliente.nombre, 'Héctor')
        self.assertEqual(nuevo_cliente.apellido, 'Costa')
        
