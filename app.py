from flask import Flask, render_template, request, redirect, url_for, flash, session 

app = Flask(__name__)
app.secret_key = "tu_clave_secreta"
#Usuarios predefinidos (simulando base de datos)
USUARIOS_REGISTRADOS = {
    'admin@gmail.com' : {
        'password' : 'Admin123',
        'nombre' : 'Administrador',
        'fecha_nacimiento' : '1985-11-28'
    },
    'usuario@correo.com' : {
        'password' : 'usuario123',
        'nombre' : 'Karime Cruz',
        'fecha_nacimiento' : '2009-12-17'
    } 
}

app.config['SECRET_KEY'] = 'Mimecita123'

@app.route('/')
def index():
    return render_template("index.html")



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

@app.route('/iniciodesesion')
def login():
    if session.get('iniciodesesion') == True:
        session.clear()
        return render_template("index.html")
    return render_template("iniciodesesion.html")

@app.route('/validainiciodesesion', methods=['GET','POST'])
def iniciodesesion():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
    
    #VALIDAR CREDENCIALES
    if not email or not password:
        flash('por favor ingresa email y contraseña','error')
    elif email in USUARIOS_REGISTRADOS:
        usuario = USUARIOS_REGISTRADOS[email]
        if usuario['password'] == password:
            #CREDENCIALES CORRECTAS
            session

        if usuario and usuario['password'] == password:
            session['usuario'] = usuario['nombre']
            flash("Inicio de sesión exitoso")
            return redirect(url_for('index'))
        else:
            flash("Correo o contraseña incorrectos")
            return render_template('index.html')

    return render_template("iniciodesesion.html")


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        error = None
        Nombre = request.form.get("nombre")
        Apellido = request.form.get("apellido")
        fecha = request.form.get("fecha")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        genero = request.form.get("genero")

        if password != confirmPassword:
            error = "Las contraseñas no coincidenn" 

        if error is not None:
            flash(error)
            return render_template('registro.html')
        else:
            flash(f"Registro exitoso!: {Nombre}")
            return render_template('index.html')
    
    return render_template('registro.html') 



if __name__ == "__main__":
    app.run(debug=True) 