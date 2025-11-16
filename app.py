from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__, template_folder="templates")

def cargar_paises(ruta_csv):
    paises = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Normalizar y convertir tipos
            fila['pais'] = fila.get('pais', '').strip()
            # poblacion como entero seguro
            try:
                fila['poblacion'] = int(float(fila.get('poblacion', 0)))
            except:
                fila['poblacion'] = 0
            # superficie como entero seguro
            try:
                fila['superficie'] = int(float(fila.get('superficie', 0)))
            except:
                fila['superficie'] = 0
            fila['continente'] = fila.get('continente', '').strip()
            paises.append(fila)
    return paises

@app.route('/', methods=['GET', 'POST'])
def mostrar_paises():
    ruta_csv = os.path.join(os.path.dirname(__file__), "paises.csv")
    paises = cargar_paises(ruta_csv)

    # Obtener lista de continentes únicos (para el select)
    continentes = sorted({p['continente'] for p in paises if p['continente']})

    # Valores por defecto de los filtros
    filtros = {
        'search': '',
        'continente': 'todos',
        'pop_cmp': 'gte',      # 'gte' >= , 'lte' <=
        'pop_val': '',
        'surf_cmp': 'gte',
        'surf_val': ''
    }

    if request.method == 'POST':
        # Si se pulsa restablecer -> volvemos a lista completa
        if request.form.get('restablecer'):
            # dejar filtros en defaults (ya están)
            pass
        else:
            # leer filtros enviados (mantenerlos para la UI)
            filtros['search'] = request.form.get('busqueda', '').strip()
            filtros['continente'] = request.form.get('continente', 'todos')
            filtros['pop_cmp'] = request.form.get('pop_cmp', 'gte')
            filtros['pop_val'] = request.form.get('pop_val', '').strip()
            filtros['surf_cmp'] = request.form.get('surf_cmp', 'gte')
            filtros['surf_val'] = request.form.get('surf_val', '').strip()

            # Aplicar filtros acumulativos sobre la lista original
            resultados = paises

            # 1) Buscador por nombre (si hay)
            if filtros['search']:
                q = filtros['search'].lower()
                resultados = [p for p in resultados if q in p['pais'].lower()]

            # 2) Filtrar por continente (si no es 'todos')
            if filtros['continente'] and filtros['continente'].lower() != 'todos':
                cont = filtros['continente'].lower()
                resultados = [p for p in resultados if p['continente'].lower() == cont]

            # 3) Filtrar por población (si se indicó un número válido)
            if filtros['pop_val']:
                try:
                    val = int(float(filtros['pop_val']))
                    if filtros['pop_cmp'] == 'gte':
                        resultados = [p for p in resultados if p['poblacion'] >= val]
                    else:
                        resultados = [p for p in resultados if p['poblacion'] <= val]
                except:
                    # valor inválido -> ignorar filtro
                    pass

            # 4) Filtrar por superficie (si se indicó un número válido)
            if filtros['surf_val']:
                try:
                    val = int(float(filtros['surf_val']))
                    if filtros['surf_cmp'] == 'gte':
                        resultados = [p for p in resultados if p['superficie'] >= val]
                    else:
                        resultados = [p for p in resultados if p['superficie'] <= val]
                except:
                    pass

            paises = resultados

    # En GET o después de restablecer, paises ya contiene la lista completa

    return render_template(
    'index.html',
    paises=paises,
    continentes=continentes,
    filtros=filtros
     )

if __name__ == '__main__':
    app.run(debug=True)
