from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/iniciodesesion')
def iniciodesesion():
    return render_template("iniciodesesion.html") 

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/vehiculos')
def vehiculos():
    return render_template("vehiculos.html")

@app.route('/animales')
def animales():
    return render_template("animales.html")

@app.route('/maravillas')
def maravillas():
    return render_template("maravillas.html")

@app.route('/acerca')
def acerca():
    return render_template("acerca.html")


if __name__ == "__main__":
    app.run(debug=True)