
Calculadora API - Programación III
Este proyecto es una API desarrollada con FastAPI para el curso de Programación III. Esta API permite realizar operaciones matemáticas básicas ediante endpoints de tipo get.

>Requisitos:

- Python 3.10+
- Entorno virtual activo
- Dependencias: FastAPI, Uvicorn, Pytest

>Instalación y Configuración:

    1. Clonar el repositorio
        git clone https://github.com/Mitzy521/calculator-api.git
        cd calculator.api

    2. Crear y activar el entorno virtual
       :Windows
       python -m venv venv
       venv\Scripts\activate

    3. Instalar dependencias
       pip install -r requierements.txt

    4. Ejecutar la API
       uvicorn app.main:app --reload

>Endpoints Disponibles:

    OPERACIÓN----------MÉTODO--------ENDPOINT----------PARÁMETROS
    Suma                GET           /sum             num1, num2
    Resta               GET           /subtract        num1, num2
    Multiplicación      GET           /Multiply        num1, num2
    División            GET

>Ejemplo de uso (Suma):

GET /sum? num1=10 & num2=5
Respuesta: {"operation": "sum", "num1": 10, "num2": 5, "result": 15}

Ejemplo de uso
GET /multiplicar/2/3
Respuesta:
{
  "resultado": 6
}

>Pruebas automatizadas

Para verificar que todo funcione correctamente y que el manejo de errores (como la división por cero) sea válido, ejecuta:
pytest

>Colaboradores y Flujo de Trabajo

    Flujo de trabajo:
        1. Fork del repositorio principal
        2. Creación de una rama la nueva funcionalidad:
            nombre-rama/nombre-operación
        3. Realizar el Pull Request para revsión y merge

>Integrantes

    - Mitzy Yuridia Cu Chén
    - Jefferson Nimrod Perez Dominguez
