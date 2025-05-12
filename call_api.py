from gradio_client import Client

# Conecta con tu Space
client = Client("HBAB/proyecto")

# Enviar código para analizar
resultado = client.predict(
    codigo="""
def on_btn_historial_clicked(self):
    QMessageBox.information(self, "Historial", "Botón Historial clickeado")
""",
    api_name="/predict"
)

# Imprimir resultados
print("🧪 Sintaxis:", resultado[0])
print("📘 Análisis lógico:", resultado[1])
