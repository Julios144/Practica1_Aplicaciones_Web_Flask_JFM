from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    #nombre
    nombre=request.form.get("nombre")
    #correo
    #apellidos=request.form.get("apellidos")
    correo=request.form.get("correo")
    #mensaje
    mensaje=request.form.get("mensaje")

    #curso =request.form.getlist("curso")
    return render_template("contacto.html",nom=nombre,co=correo,mensa=mensaje)

if __name__ == '__main__':
    app.run(debug=True)