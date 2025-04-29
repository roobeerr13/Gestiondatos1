import sys

DATABASE_PATH = 'clientes.csv'
if 'unittest' in sys.argv[0]:
    DATABASE_PATH = 'clientes_test.csv'