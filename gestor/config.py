import sys

DATABASE_PATH = 'gestor/clientes.csv'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'gestor/tests/clientes_test.csv'


import os


DATABASE_PATH = os.path.join(os.path.dirname(__file__), "clientes.csv")