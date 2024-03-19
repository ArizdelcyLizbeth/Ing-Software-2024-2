from flask import Blueprint, render_template, request, flash, url_for, redirect
from datetime import datetime, timedelta, date
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Usuarios import Usuarios
from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

"""
Rentals are modified by ID in order to avoid possible mistakes.
"""

# Route to see rentals -> localhost:5001/renta/
@renta_blueprint.route('/')
def view_rents():
    try:
        rents = Rentar.query.all()
        rents_data = []
        for rent in rents:
            expiry_date = rent.fecha_renta + timedelta(days=rent.dias_de_renta)
            past_rent = expiry_date < datetime.combine(date.today(), datetime.min.time())
            rents_data.append({'rent': rent, 'past_rent': past_rent})
        return render_template('rentals/rents.html', rents=rents_data)
    except Exception as e:
        print("An error occurred:", str(e))
        return "An error occurred. Please try again later."

# Route to add a rental -> localhost:5001/renta/agregar
@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def add_rental():
    if request.method == 'GET':
        return render_template('rentals/rent_add.html')
    else:
        try:
            user_id = request.form.get('user_id')
            movie_id = request.form.get('movie_id')
            rent_date = request.form.get('rent_date')
            rent_days = request.form.get('rent_days')
            status = True if request.form.get('status') else False
            if not user_id or not movie_id:
                flash('Missing fields', 'error')
                return redirect(url_for('renta.add_rental'))
            user = Usuarios.query.filter_by(idUsuario=user_id).first()
            if not user:
                flash('User is not registered', 'error')
                return redirect(url_for('renta.add_rental'))
            movie = Peliculas.query.filter_by(idPelicula=movie_id).first()
            if not movie:
                flash('Movie is not registered', 'error')
                return redirect(url_for('renta.add_rental'))
            rent_date = rent_date or date.today()
            rent_days = int(rent_days) if rent_days else 5
            new_rental = Rentar(idUsuario=user_id, idPelicula=movie_id, fecha_renta=rent_date, dias_de_renta=rent_days, estatus=status)
            db.session.add(new_rental)
            db.session.commit()
            flash('Rental added successfully', 'success')
            return redirect(url_for('renta.view_rents'))
        except Exception as e:
            flash(f'An error occurred while adding rental: {str(e)}', 'error')
            return redirect(url_for('renta.add_rental'))

# Route to modify rental -> localhost:5001/renta/modificar
@renta_blueprint.route('/modificar', methods=['GET', 'POST'])
def modify_rental():
    if request.method == 'POST':
        try:
            rent_id = int(request.form.get('rent_id'))
            return redirect(url_for('renta.modify_rental_id', id=rent_id))
        except ValueError:
            flash('Ops! Invalid ID, please enter a valid ID again', 'error')
            return redirect(url_for('renta.modify_rental'))
    return render_template('rentals/rent_id.html')

# Route to modify rental by ID -> localhost:5001/renta/modificar/<int:id>
@renta_blueprint.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modify_rental_id(id):
    try:
        rental = Rentar.query.get(id)
        if not rental:
            return render_template('rentals/rent_not_found.html')
        if request.method == 'GET':
            return render_template('rentals/rent_modify.html', rental=rental)
        elif request.method == 'POST':
            rental.status = True if request.form.get('status') else False
            db.session.commit()
            flash('Rental modified successfully', 'success')
            return redirect(url_for('renta.view_rents'))
    except Exception as e:
        flash(f'An error occurred while modifying rental: {str(e)}', 'error')
        return redirect(url_for('renta.view_rents'))