import os
import platform
import re

def limpiar_pantalla():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
	if mensaje:
		print(mensaje)
	while True:
		texto = input("> ")
		if longitud_min <= len(texto) <= longitud_max:
			return texto

def dni_valido(dni, lista):
	if not re.match('[0-9]{2}[A-Z]$', dni):
		print("DNI incorrecto, debe cumplir el formato.")
		return False
	for cliente in lista:
		if cliente.dni == dni:
			print("DNI utilizado por otro cliente.")
			return False
	return True