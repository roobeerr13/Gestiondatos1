import os
import platform
import re

def limpiar_pantalla():
    os.system("cls") if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None, texto=None):
    if texto is not None:
        # Modo para tests o GUI: validar el texto proporcionado
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        return None
    # Modo interactivo (terminal)
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def dni_valido(dni, lista):
    if not re.match(r'[0-9]{2}[A-Z]$', dni):
        return False
    for cliente in lista:
        if cliente.dni == dni:
            return False
    return True