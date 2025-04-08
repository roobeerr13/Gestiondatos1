import os
import platform

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