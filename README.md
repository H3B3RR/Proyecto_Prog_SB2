
# Proyecto de Análisis de Código en Python

Este proyecto proporciona una herramienta para analizar código Python y detectar errores de sintaxis y problemas lógicos utilizando la API de Hugging Face y el modelo de análisis semántico `Salesforce/codet5-base`.

## Características

- **Análisis de Sintaxis**: Detecta errores de sintaxis en el código Python proporcionado.
- **Análisis Lógico/semántico**: Utiliza un modelo de Hugging Face para analizar problemas lógicos o semánticos en el código.
- **Interfaz de Línea de Comandos**: El código se lee desde un archivo de texto, se envía a la API y el resultado se guarda en otro archivo de texto.
- **Fácil de Usar**: Simplemente ingresa tu código en un archivo de texto y ejecuta el script desde la terminal.

## Requisitos

- **Python 3.6 o superior**.
- **Librerías necesarias**:
  - `gradio_client`
  - `requests`
  
Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install gradio_client requests
````

## Archivos

* **`entrada.txt`**: Este archivo debe contener el código Python que deseas analizar.
* **`salida.txt`**: Este archivo contiene el resultado del análisis de sintaxis y el análisis lógico del código proporcionado. Se genera automáticamente.

## ¿Cómo ejecutar el script?

1. **Clona el repositorio**:

   Si aún no tienes el proyecto, puedes clonarlo desde GitHub:

   ```bash
   git clone https://github.com/H3B3RR/Proyecto_Prog_SB2.git
   cd tu_repositorio
   ```

2. **Prepara el archivo de entrada**:

Crea un archivo llamado `entrada.txt` en el directorio del proyecto. Este archivo debe contener el código Python que deseas analizar. A continuación, se presentan tres ejemplos:

### Ejemplo 1: Código Correcto
```python
def saludar(nombre):
    print(f"Hola, {nombre}!")
```

### Ejemplo 2: Código con Error Semántico
```python
def dividir(a, b):
    return a / b  # No se maneja la división por cero
```

### Ejemplo 3: Código con Error de Sintaxis
```python
def sumar(a, b)
    return a + b
```

3. **Ejecuta el script**:

    En la terminal, navega al directorio donde se encuentra el archivo `call_api.py` y ejecuta el siguiente comando:

    ```bash
    python call_api.py
    ```

4. **Revisa los resultados**:

    El script generará un archivo `salida.txt` en el mismo directorio, que contiene el análisis de sintaxis y análisis lógico del código que proporcionaste.

    **Nota**: El análisis puede tardar entre 3 y 10 minutos debido a que la infraestructura utilizada es limitada, ya que se trata de la versión gratuita.

    El archivo `salida.txt` tendrá el siguiente formato:

    ```
    🧪 Sintaxis:
    ✅ Sintaxis válida

    📘 Análisis lógico:
    Este código parece estar bien en términos lógicos, aunque el comportamiento puede depender de los detalles del entorno de la GUI.
    ```

## Ejemplo de uso

### 1. Crea un archivo `entrada.txt` con el siguiente contenido:

```python
def ejemplo_funcion():
    print("Hola mundo")
```

### 2. Ejecuta el script con:

```bash
python call_api.py
```

### 3. El resultado en `salida.txt` será algo similar a:

```
🧪 Sintaxis:
✅ Sintaxis válida

📘 Análisis lógico:
El código parece correcto en términos lógicos.
```

## Notas

* El modelo de Hugging Face utilizado para el análisis lógico es bastante efectivo para detectar errores semánticos comunes, pero no garantiza que todos los errores lógicos sean identificados, especialmente en casos complejos.
* La API puede tener limitaciones dependiendo del tráfico o de las restricciones de uso en Hugging Face.



## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.


## API y Funcionamiento Interno

El análisis de código se realiza utilizando una API basada en Hugging Face y Gradio. A continuación, se describe cómo funciona:

### Implementación de la API

La API está diseñada para analizar código Python y proporcionar dos tipos de análisis: sintáctico y semántico. A continuación, se detalla el funcionamiento:

```python
import gradio as gr
import ast
from transformers import pipeline
import pyflakes.api
from pyflakes.reporter import Reporter
import io

# Cargar modelo de Hugging Face para análisis semántico
analyzer = pipeline("text2text-generation", model="Salesforce/codet5-base")

# Función que analiza el código
def analizar_codigo(codigo):
    errores = ""
    explicacion = ""

    # Verificación de sintaxis con pyflakes
    reporter_output = io.StringIO()
    reporter = Reporter(reporter_output, reporter_output)
    try:
        # Analizar código con pyflakes
        pyflakes.api.check(codigo, filename="<input>", reporter=reporter)
        errores_sintaxis = reporter_output.getvalue()

        if errores_sintaxis:
            errores = f"❌ Errores de sintaxis detectados:\n{errores_sintaxis}"
            explicacion = "Revisa los errores de sintaxis indicados y corrígelos antes de continuar."
            return errores, explicacion
        else:
            errores = "✅ Sintaxis válida"
    except Exception as e:
        errores = f"❌ Error al analizar la sintaxis: {str(e)}"
        explicacion = "Hubo un problema al analizar la sintaxis del código. Asegúrate de que el código sea correcto."

    # Análisis semántico con modelo
    prompt = f"Analiza el siguiente código en Python y explica si hay errores lógicos o semánticos:\n\n{codigo}"
    try:
        resultado = analyzer(prompt, max_length=256, do_sample=False)[0]['generated_text']
        return errores, resultado
    except Exception as e:
        return errores, f"❌ Error al analizar semánticamente el código: {str(e)}"

# ⬇️ Interfaz Gradio
demo = gr.Interface(
    fn=analizar_codigo,
    inputs=gr.Textbox(lines=15, label="Pega tu función aquí"),
    outputs=[
        gr.Textbox(label="Estado de la sintaxis"),
        gr.Textbox(label="Análisis semántico (lógico)")
    ],
    title="🔍 Analizador de errores en funciones de programación",
    description="Este Space detecta errores de sintaxis y semánticos (lógicos) en funciones en Python."
)

demo.launch()
```

### Dependencias

Para que la API funcione correctamente, asegúrate de instalar las siguientes dependencias:

```bash
pip install gradio transformers torch pyflakes
```

### Descripción del Proceso

1. **Análisis de Sintaxis**:
   - Se utiliza la librería `pyflakes` para verificar errores de sintaxis en el código proporcionado.
   - Si se detectan errores, se devuelven al usuario con una explicación.

2. **Análisis Semántico**:
   - Se utiliza el modelo `Salesforce/codet5-base` de Hugging Face para analizar el código y detectar posibles errores lógicos o semánticos.
   - El modelo genera una explicación detallada basada en el código proporcionado.

3. **Interfaz Gradio**:
   - La API incluye una interfaz gráfica creada con `gradio`, donde los usuarios pueden pegar su código Python y recibir el análisis en tiempo real.

### Requisitos Adicionales

Asegúrate de incluir las siguientes librerías en el archivo `requirements.txt`:

```
gradio
transformers
torch
pyflakes
```

Con esta implementación, puedes analizar código Python de manera eficiente y obtener información detallada sobre posibles errores de sintaxis y lógica. 
