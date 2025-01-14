from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = round((nota1 + nota2 + nota3) / 3, 2)

            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"
        except ValueError:
            promedio = "Error en las notas ingresadas"
            estado = "Error"

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombres = []
    nombres_max = []
    caracteres_max = 0

    if request.method == 'POST':
        try:
            nombre1 = request.form['nombre1']
            nombre2 = request.form['nombre2']
            nombre3 = request.form['nombre3']

            if not (nombre1.isalpha() and nombre2.isalpha() and nombre3.isalpha()):
                raise ValueError("Los nombres deben contener solo letras.")

            nombres = [nombre1, nombre2, nombre3]

            caracteres_max = max(len(nombre) for nombre in nombres)
            nombres_max = [nombre for nombre in nombres if len(nombre) == caracteres_max]

        except ValueError as e:
            nombres_max = ["Error: " + str(e)]
            caracteres_max = None

    return render_template(
        'ejercicio2.html',
        nombres_max=nombres_max,
        caracteres_max=caracteres_max
    )

if __name__ == '__main__':
    app.run(debug=True)








