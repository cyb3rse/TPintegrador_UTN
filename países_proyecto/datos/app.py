from flask import Flask, render_template, request
import csv
import os

# Inicialización de Flask
app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def mostrar_paises():
    paises = []
    ruta_csv = os.path.join(os.path.dirname(__file__), "paises.csv")

    # Leer el CSV
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append(fila)

    # Si se envió una búsqueda
    busqueda = ""
    if request.method == 'POST':
        busqueda = request.form.get('busqueda', '').lower()
        paises = [p for p in paises if busqueda in p['pais'].lower()]

    # Enviar datos al HTML
    return render_template('index.html', paises=paises)

if __name__ == '__main__':
    app.run(debug=True)
