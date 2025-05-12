from gradio_client import Client

# Conectar con tu Space en Hugging Face
client = Client("HBAB/proyecto")

# Función para analizar el código
def analizar_codigo():
    # Leer el código desde el archivo de entrada
    with open('input.txt', 'r') as file:
        codigo = file.read()

    # Enviar el código a la API
    resultado = client.predict(codigo=codigo, api_name="/predict")

    # Guardar el resultado en el archivo de salida
    with open('out.txt', 'w') as file:
        file.write("🧪 Sintaxis:\n" + resultado[0] + "\n\n")
        file.write("📘 Análisis lógico:\n" + resultado[1])

    print("El análisis se ha guardado en 'out.txt'.")

# Ejecutar la función
if __name__ == "__main__":
    analizar_codigo()
