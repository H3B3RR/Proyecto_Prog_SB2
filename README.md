# Proyecto_Prog_SB2
Este proyecto es un analizador de código Python que verifica errores de sintaxis y semántica (lógica) en funciones de programación.


# Documentación del Proyecto: Analizador Sintáctico y Semántico
## Autor del Proyecto

Este proyecto fue desarrollado por [Heber Nolasco](https://github.com/tu-usuario-de-github). Si tienes preguntas o sugerencias, no dudes en abrir un issue o contactarme a través de mi perfil de GitHub.

## Descripción del Proyecto
Este proyecto es un analizador de código Python que verifica errores de sintaxis y semántica (lógica) en funciones de programación. Utiliza herramientas como:

- **Pyflakes**: Para verificar errores de sintaxis.
- **Hugging Face Transformers**: Para realizar análisis semántico utilizando el modelo `Salesforce/codet5-base`.
- **Gradio**: Para crear una interfaz gráfica interactiva que permite a los usuarios pegar su código y obtener resultados en tiempo real.

## Características

### Análisis de Sintaxis
- Detecta errores de sintaxis en el código utilizando `pyflakes`.
- Proporciona mensajes claros sobre los errores encontrados.

### Análisis Semántico
- Utiliza un modelo de lenguaje (`codet5-base`) para analizar el código y detectar posibles errores lógicos o semánticos.
- Ofrece explicaciones detalladas sobre los problemas encontrados.

### Interfaz Gráfica
- Implementada con `Gradio`, permite a los usuarios interactuar fácilmente con el analizador.
- Los resultados se presentan en dos secciones:
    - **Estado de la Sintaxis**: Indica si la sintaxis es válida o si hay errores.
    - **Análisis Semántico**: Explica posibles errores lógicos en el código.

## Requisitos del Proyecto
Para ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Archivo `requirements.txt`.

## Instalación de Dependencias
Ejecuta el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Cómo Ejecutar el Proyecto
1. Asegúrate de que todas las dependencias estén instaladas.
2. Ejecuta el archivo `app.py` con el siguiente comando:

```bash
python app.py
```

Esto abrirá una interfaz gráfica en tu navegador donde podrás pegar tu código Python para analizarlo.

## Ejemplos de Código para Probar

### 1. Código Correcto
Este código no tiene errores de sintaxis ni semánticos.

```python
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)
```

**Resultado Esperado**:
- **Estado de la Sintaxis**: ✅ Sintaxis válida.
- **Análisis Semántico**: No se detectan errores lógicos.

### 2. Código con Error Semántico
Este código tiene un error lógico: intenta dividir por cero, lo cual generará un error en tiempo de ejecución.

```python
def division(a, b):
    return a / b

resultado = division(5, 0)
print(resultado)
```

**Resultado Esperado**:
- **Estado de la Sintaxis**: ✅ Sintaxis válida.
- **Análisis Semántico**: ❌ Error lógico detectado: división por cero.

### 3. Código con Error Sintáctico
Este código tiene un error de sintaxis: falta un paréntesis de cierre en la definición de la función.

```python
def saludo(nombre:
    print(f"Hola, {nombre}")
```

**Resultado Esperado**:
- **Estado de la Sintaxis**: ❌ Error de sintaxis detectado: falta un paréntesis de cierre.
- **Análisis Semántico**: No se realiza debido a errores de sintaxis.

## Cómo Probar los Ejemplos
1. Copia cada ejemplo de código y pégalo en el cuadro de texto de la interfaz gráfica de `Gradio`.
2. Observa los resultados en las secciones:
    - **Estado de la Sintaxis**: Indica si la sintaxis es válida o si hay errores.
    - **Análisis Semántico**: Explica posibles errores lógicos en el código.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

```
integrador/
├── app.py
├── requirements.txt
├── README.md
└── modelos/
    └── codet5-base/
```

## Notas Adicionales
- Si encuentras problemas al ejecutar el proyecto, asegúrate de que las dependencias estén correctamente instaladas.
- El modelo `Salesforce/codet5-base` requiere conexión a Internet para descargarse la primera vez que se utiliza.
