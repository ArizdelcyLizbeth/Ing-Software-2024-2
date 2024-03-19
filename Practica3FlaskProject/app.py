from contollers.PeliculaController import pelicula_blueprint
from contollers.UsuarioController import usuario_blueprint
from contollers.RentaController import renta_blueprint
from flask import Flask, render_template
from alchemyClasses import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(renta_blueprint)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/usuario/agregar', methods=['GET'])
def add_user_form():
    return render_template('usuarios/add_user.html')

# Ruta y función para procesar la solicitud de agregar un nuevo usuario
@app.route('/usuario/agregar', methods=['POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        password = request.form['password']
        email = request.form['email']
        return redirect(url_for('view_users'))

if __name__ == '__main__':
    app.run()