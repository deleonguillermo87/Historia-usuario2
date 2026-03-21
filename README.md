📦 Sistema de Inventario Básico en Python

📖 Descripción

Este proyecto consiste en un sistema de inventario desarrollado en Python que permite registrar múltiples productos, almacenarlos en una lista y calcular estadísticas generales del inventario.

El programa permite al usuario interactuar mediante un menú, donde puede:
	•	Registrar productos
	•	Visualizar el inventario
	•	Calcular estadísticas generales

Cada producto contiene:
	•	Nombre del producto
	•	Precio unitario
	•	Cantidad disponible

El sistema valida los datos ingresados para evitar errores y muestra la información de forma clara.

Este proyecto está diseñado con fines educativos, ideal para personas que están comenzando a aprender programación en Python.

⸻

🎯 Objetivos del Proyecto
	•	Practicar conceptos básicos de programación en Python.
	•	Implementar validación de datos ingresados por el usuario.
	•	Comprender el uso de estructuras de control como bucles (while).
	•	Aplicar manejo de errores con try y except.
	•	Utilizar estructuras de datos como listas y diccionarios.
	•	Desarrollar lógica para el cálculo de estadísticas en un sistema real.

⸻

⚙️ Características

✅ Menú interactivo continuo
✅ Registro de múltiples productos
✅ Almacenamiento en lista de diccionarios
✅ Validación de nombre (solo letras)
✅ Validación de precio (número positivo)
✅ Validación de cantidad (entero positivo)
✅ Manejo de errores en entradas del usuario
✅ Visualización completa del inventario
✅ Cálculo de estadísticas del inventario
✅ Control de opciones inválidas

⸻

🗂️ Estructura del Proyecto
inventario-python/
│
├── inventario.py   # Código principal del sistema
└── README.md       # Documentación del proyecto


💻 Requisitos

Para ejecutar este programa necesitas:
	•	Python 3.x

Puedes descargarlo desde:
https://www.python.org/downloads/

Para verificar la instalación:
python --version

▶️ Instalación y Ejecución

1️⃣ Clonar el repositorio
git clone https://github.com/tuusuario/inventario-python.git

2️⃣ Acceder a la carpeta del proyecto
cd inventario-python

3️⃣ Ejecutar el programa
python inventario.py

🖥️ Funcionalidades del Sistema

🔹 1. Agregar producto

Permite registrar un producto solicitando:
	•	Nombre (solo letras)
	•	Precio (número positivo)
	•	Cantidad (entero positivo)

Los datos se almacenan en un diccionario y se agregan a una lista.

⸻

🔹 2. Ver inventario

Muestra todos los productos registrados con:
	•	Nombre
	•	Precio
	•	Cantidad

Si no hay productos, el sistema lo indica.

⸻

🔹 3. Calcular estadísticas

El sistema calcula automáticamente:
	•	Total de productos registrados
	•	Cantidad total de unidades
	•	Valor total del inventario

Fórmula utilizada:
Valor total = precio × cantidad

🔹 4. Salir

Finaliza la ejecución del programa.

🖥️ Ejemplo de ejecución
=== SISTEMA DE INVENTARIO ===

opciones disponible
1. desea agregrar un producto
2. desea ver el inventario
3. desea calcular estadisticas
4. salir...

elegir la opcion : 1

Ingrese el nombre del producto: Laptop
Ingrese el precio del producto: 850.75
Ingrese la cantidad del producto: 2

elegir la opcion : 2

Laptop 850.75 2

elegir la opcion : 3

Total de productos registrados: 1
Cantidad total de unidades: 2
Valor total del inventario: 1701.5

