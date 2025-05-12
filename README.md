
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
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Prepara el archivo de entrada**:

   Crea un archivo llamado `entrada.txt` en el directorio del proyecto. Este archivo debe contener el código Python que deseas analizar. Ejemplo de contenido:

   ```python
   def on_btn_historial_clicked(self):
       QMessageBox.information(self, "Historial", "Botón Historial clickeado")
   ```

3. **Ejecuta el script**:

   En la terminal, navega al directorio donde se encuentra el archivo `call_api.py` y ejecuta el siguiente comando:

   ```bash
   python call_api.py
   ```

4. **Revisa los resultados**:

   El script generará un archivo `salida.txt` en el mismo directorio, que contiene el análisis de sintaxis y análisis lógico del código que proporcionaste.

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

## Contribuciones

Si deseas contribuir a este proyecto, por favor, haz un fork, crea una rama y envía un pull request. Asegúrate de seguir las mejores prácticas de codificación y pruebas.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

```

### ¿Qué incluye este README?

1. **Descripción general**: Qué hace el proyecto y las funcionalidades clave.
2. **Requisitos**: Librerías y versiones de Python necesarias para ejecutar el proyecto.
3. **Instrucciones de uso**:
   - Cómo clonar el repositorio.
   - Cómo preparar y ejecutar el script.
4. **Ejemplo de uso**: Un flujo básico para mostrar cómo interactuar con el proyecto.
5. **Notas**: Limitaciones y detalles adicionales sobre el análisis y uso del modelo.
6. **Contribuciones**: Cómo contribuir al proyecto.
7. **Licencia**: Tipo de licencia del proyecto (MIT en este caso).

Este README debería ser suficiente para que otros entiendan y puedan usar tu proyecto correctamente. ¿Te gustaría hacer alguna modificación o agregar más detalles?
```
