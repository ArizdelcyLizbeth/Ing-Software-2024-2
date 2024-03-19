from flask import Blueprint, render_template, request, flash, url_for, redirect
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuarios')

"""
Users are managed by their IDs to prevent potential mistakes.
"""

# Route to view users -> localhost:5001/usuarios/
@usuario_blueprint.route('/')
def view_users():
    usuarios = Usuarios.query.all()
    return render_template('usuarios/view_users.html', usuarios=usuarios)

# Route to add a user -> localhost:5001/usuarios/add
@usuario_blueprint.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('usuarios/add_user.html')
    else:
        try:
            nombre = request.form.get('nombre')
            apPat = request.form.get('apPat')
            apMat = request.form.get('apMat')
            password = request.form.get('password')
            email = request.form.get('email')
            superUser = bool(request.form.get('superUser'))
            if not all((nombre, apPat, password, email)):
                flash('Please fill in all required fields', 'error')
                return redirect(url_for('usuario.add_user'))
            if Usuarios.query.filter_by(email=email).first():
                flash('An account with this email address already exists', 'error')
                return render_template('usuarios/add_user.html')
            new_user = Usuarios(nombre=nombre, apPat=apPat, apMat=apMat, password=password, email=email, superUser=superUser)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully', 'success')
            return redirect(url_for('usuario.view_users'))
        except Exception as e:
            flash(f'Error adding user: {str(e)}', 'error')
            return redirect(url_for('usuario.add_user'))

# Route to modify user -> localhost:5001/usuarios/modify
@usuario_blueprint.route('/modify', methods=['GET', 'POST'])
def modify_user():
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')
        try:
            id_usuario = int(id_usuario)
            return redirect(url_for('usuario.modify_user_by_id', id=id_usuario))
        except ValueError:
            flash('Invalid ID, please enter a valid ID', 'error')
    return render_template('usuarios/user_id.html')

# Route to modify user by id -> localhost:5001/usuarios/modify/<int:id>
@usuario_blueprint.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify_user_by_id(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        return render_template('usuarios/user_not_found.html')
    if request.method == 'GET':
        return render_template('modify_user.html', usuario=usuario)
    elif request.method == 'POST':
        new_email = request.form['email']
        old_email = Usuarios.query.filter(
            (Usuarios.email == new_email) & (Usuarios.idUsuario != usuario.idUsuario)).first()
        if old_email:
            flash('This email address is already in use', 'error')
            return render_template('modify_user.html', usuario=usuario)
        usuario.nombre = request.form['nombre']
        usuario.apPat = request.form['apPat']
        usuario.apMat = request.form['apMat']
        usuario.password = request.form['password']
        usuario.email = new_email
        usuario.superUser = bool(request.form.get('superUser'))
        if not all((usuario.nombre, usuario.apPat, usuario.password, usuario.email)):
            flash('Please fill in all required fields', 'error')
            return render_template('modify_user.html', usuario=usuario)
        try:
            db.session.commit()
            flash('User modified successfully', 'success')
            return redirect(url_for('usuario.view_users'))
        except Exception as e:
            flash(f'Error modifying user: {str(e)}', 'error')
            return render_template('modify_user.html', usuario=usuario)

# Route to delete user -> localhost:5001/usuarios/delete
@usuario_blueprint.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')
        try:
            id_usuario = int(id_usuario)
            return redirect(url_for('usuario.delete_user_by_id', id=id_usuario))
        except ValueError:
            flash('Invalid ID, please enter a valid ID', 'error')
    return render_template('usuarios/user_id.html')

# Route to delete user by id -> localhost:5001/usuarios/delete/<int:id>
@usuario_blueprint.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_user_by_id(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        return render_template('usuarios/user_not_found.html')
    rentas = Rentar.query.filter_by(idUsuario=usuario.idUsuario).all()
    if rentas:
        flash('Cannot delete user as they have associated rentals', 'error')
    else:
        try:
            db.session.delete(usuario)
            db.session.commit()
            flash('User deleted successfully', 'success')
        except Exception as e:
            flash(f'Error deleting user: {str(e)}', 'error')
    return redirect(url_for('usuario.view_users'))
