import os
import platform
import re

def limpiar_pantalla():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')

def leer_texto(longitud_min, longitud_max, texto):
    """
    Valida si el texto tiene la longitud correcta y sigue el formato de DNI (2 dígitos + 1 letra).
    Args:
        longitud_min (int): Longitud mínima permitida.
        longitud_max (int): Longitud máxima permitida.
        texto (str): Texto a validar.
    Returns:
        bool: True si el texto es válido, False si no.
    """
    if not isinstance(texto, str):
        return False
    if len(texto) < longitud_min or len(texto) > longitud_max:
        return False
    # Verificar formato: 2 dígitos + 1 letra
    return bool(re.match(r'^\d{2}[A-Za-z]$', texto))

def dni_valido(dni, lista):
	if not re.match('[0-9]{2}[A-Z]$', dni):
		print("DNI incorrecto, debe cumplir el formato.")
		return False
	for cliente in lista:
		if cliente.dni == dni:
			print("DNI utilizado por otro cliente.")
			return False
	return True