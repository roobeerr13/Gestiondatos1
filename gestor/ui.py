import gradio as gr
import gestor.database as db
import gestor.helpers as helpers
import pandas as pd
import sys

def listar_clientes():
    if not db.Clientes.lista_clientes:
        return "No hay clientes registrados.", None
    # Convertir la lista de clientes a un DataFrame para mostrar como tabla
    data = [(c.dni, c.nombre, c.apellido) for c in db.Clientes.lista_clientes]
    df = pd.DataFrame(data, columns=["DNI", "Nombre", "Apellido"])
    return "Lista de clientes:", df

def buscar_cliente(dni):
    if not dni:
        return "Por favor, ingresa un DNI."
    dni = dni.upper()
    if not helpers.dni_valido(dni, []):  # Solo validar formato, no duplicados
        return "DNI inválido. Debe tener el formato: 2 dígitos + 1 letra (ej. 12A)."
    cliente = db.Clientes.buscar(dni)
    return f"Cliente encontrado: {cliente}" if cliente else "Cliente no encontrado."

def validar_dni(dni, lista):
    if not helpers.dni_valido(dni, lista):
        return False, "DNI inválido o ya existe. Debe tener el formato: 2 dígitos + 1 letra (ej. 12A) y no estar registrado."
    return True, ""

def validar_texto(texto, campo, min_len=2, max_len=30):
    if not texto.isalpha() or len(texto) < min_len or len(texto) > max_len:
        return False, f"{campo} debe tener solo letras y entre {min_len} y {max_len} caracteres."
    return True, ""

def añadir_cliente(dni, nombre, apellido):
    if not dni or not nombre or not apellido:
        return "Por favor, completa todos los campos."
    dni = dni.upper()
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()

    # Validar DNI
    dni_valido, dni_error = validar_dni(dni, db.Clientes.lista_clientes)
    if not dni_valido:
        return dni_error

    # Validar nombre
    nombre_valido, nombre_error = validar_texto(nombre, "Nombre")
    if not nombre_valido:
        return nombre_error

    # Validar apellido
    apellido_valido, apellido_error = validar_texto(apellido, "Apellido")
    if not apellido_valido:
        return apellido_error

    # Crear cliente
    db.Clientes.crear(dni, nombre, apellido)
    return "Cliente añadido correctamente."

def modificar_cliente(dni, nombre, apellido):
    if not dni or not nombre or not apellido:
        return "Por favor, completa todos los campos."
    dni = dni.upper()
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()

    # Verificar que el cliente existe
    cliente = db.Clientes.buscar(dni)
    if not cliente:
        return "Cliente no encontrado."

    # Validar nombre
    nombre_valido, nombre_error = validar_texto(nombre, "Nombre")
    if not nombre_valido:
        return nombre_error

    # Validar apellido
    apellido_valido, apellido_error = validar_texto(apellido, "Apellido")
    if not apellido_valido:
        return apellido_error

    # Modificar cliente
    db.Clientes.modificar(dni, nombre, apellido)
    return "Cliente modificado correctamente."

def borrar_cliente(dni):
    if not dni:
        return "Por favor, ingresa un DNI."
    dni = dni.upper()
    if not helpers.dni_valido(dni, []):  # Solo validar formato
        return "DNI inválido. Debe tener el formato: 2 dígitos + 1 letra (ej. 12A)."
    cliente = db.Clientes.borrar(dni)
    return "Cliente borrado correctamente." if cliente else "Cliente no encontrado."

def cerrar_programa():
    sys.exit(0)

# Interfaz con Gradio
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Gestor de Clientes - Interfaz Web")

    with gr.Tab("Listar Clientes"):
        listar_btn = gr.Button("Listar Clientes")
        listar_text = gr.Textbox(label="Mensaje")
        listar_table = gr.Dataframe(label="Clientes")
        listar_btn.click(fn=listar_clientes, outputs=[listar_text, listar_table])

    with gr.Tab("Buscar Cliente"):
        dni_buscar = gr.Textbox(label="DNI (2 dígitos + 1 letra, ej. 12A)")
        buscar_btn = gr.Button("Buscar")
        buscar_output = gr.Textbox(label="Resultado")
        buscar_btn.click(fn=buscar_cliente, inputs=dni_buscar, outputs=buscar_output)

    with gr.Tab("Añadir Cliente"):
        dni_añadir = gr.Textbox(label="DNI (2 dígitos + 1 letra, ej. 12A)")
        nombre_añadir = gr.Textbox(label="Nombre")
        apellido_añadir = gr.Textbox(label="Apellido")
        añadir_btn = gr.Button("Añadir")
        añadir_output = gr.Textbox(label="Resultado")
        añadir_btn.click(fn=añadir_cliente, inputs=[dni_añadir, nombre_añadir, apellido_añadir], outputs=añadir_output)

    with gr.Tab("Modificar Cliente"):
        dni_modificar = gr.Textbox(label="DNI (2 dígitos + 1 letra, ej. 12A)")
        nombre_modificar = gr.Textbox(label="Nombre")
        apellido_modificar = gr.Textbox(label="Apellido")
        modificar_btn = gr.Button("Modificar")
        modificar_output = gr.Textbox(label="Resultado")
        modificar_btn.click(fn=modificar_cliente, inputs=[dni_modificar, nombre_modificar, apellido_modificar], outputs=modificar_output)

    with gr.Tab("Borrar Cliente"):
        dni_borrar = gr.Textbox(label="DNI (2 dígitos + 1 letra, ej. 12A)")
        borrar_btn = gr.Button("Borrar")
        borrar_output = gr.Textbox(label="Resultado")
        borrar_btn.click(fn=borrar_cliente, inputs=dni_borrar, outputs=borrar_output)

    with gr.Tab("Salir"):
        salir_btn = gr.Button("Cerrar Programa")
        salir_btn.click(fn=cerrar_programa)

demo.launch()