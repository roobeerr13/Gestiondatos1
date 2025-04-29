# Gestiondatos1
https://github.com/roobeerr13/Gestiondatos1.git
=======

## Comprobación en Terminal

Puedes ejecutar una comprobación en la terminal para verificar si la aplicación está funcionando correctamente sin lanzar la interfaz web.

Ejecuta el siguiente comando desde el directorio raíz del proyecto:

```
python -m gestor.run -t
```

Esto realizará una comprobación sencilla, como verificar la conexión a la base de datos e imprimir el número de clientes registrados.

Si todo funciona correctamente, deberías ver un mensaje como:

```
Running terminal check...
Database connection successful. Number of clients: X
```

Reemplaza `X` con el número real de clientes en tu base de datos.

## Lanzar la Interfaz Web con Gradio

Para lanzar la interfaz web de la aplicación usando Gradio, ejecuta el siguiente comando desde el directorio raíz del proyecto:

```
python -m gestor.run
```

Esto iniciará la interfaz web de Gradio, donde podrás gestionar los clientes a través de un navegador.

Si prefieres ejecutar el script directamente desde la carpeta `gestor`, navega a esa carpeta y ejecuta:

```
python run.py
```

Para ejecutar la comprobación en terminal desde la carpeta `gestor`, usa:

```
python run.py -t
```

2
>>>>>>> eb10bcf86e94320e47f548df3d8524cc7a9a40fd
