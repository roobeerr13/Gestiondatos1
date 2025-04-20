import sys
import ui as gradio_ui
import gestor.database as db

def terminal_check():
    print("Running terminal check...")
    try:
        # Example check: list clients count
        count = len(db.Clientes.lista_clientes)
        print(f"Database connection successful. Number of clients: {count}")
    except Exception as e:
        print(f"Error during terminal check: {e}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        terminal_check()
    else:
        gradio_ui  # El lanzamiento de la interfaz ya está en gradio_ui.py

if __name__ == "__main__":
    main()
