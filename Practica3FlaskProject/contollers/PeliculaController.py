from flask import Blueprint, render_template, request, flash, url_for, redirect
from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Rentar import Rentar
from alchemyClasses import db

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

"""
Movies are deleted and modified by ID in order to avoid possible mistakes.
"""

# Route to add a movie -> localhost:5001/pelicula/agregar
@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('movies/movie_add.html')
    else:
        name = request.form.get('nombre')
        genre = request.form.get('genero')
        duration = request.form.get('duracion')
        inventory = request.form.get('inventario')
        if not name:
            flash('The name field is missing.', 'error')
            return redirect(url_for('pelicula.add_movie'))
        # Convert duration and inventory to int if provided
        duration = int(duration) if duration else None
        inventory = int(inventory) if inventory else 1
        new_movie = Peliculas(nombre=name, genero=genre, duracion=duration, inventario=inventory)
        try:
            db.session.add(new_movie)
            db.session.commit()
            flash('Movie added successfully.', 'success')
            return redirect(url_for('pelicula.view_movies'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding movie. Details: {}'.format(str(e)), 'error')
            return redirect(url_for('pelicula.add_movie'))

# Route to modify movie -> localhost:5001/pelicula/modificar
@pelicula_blueprint.route('/modificar', methods=['GET', 'POST'])
def modify_movie():
    if request.method == 'POST':
        movie_id = request.form.get('id_pelicula')
        try:
            # Convert id to int when provided
            movie_id = int(movie_id)
            return redirect(url_for('pelicula.modify_movie_id', id=movie_id))
        except ValueError:
            flash('Oops! Invalid ID, please enter a valid ID again', 'error')
            return redirect(url_for('pelicula.modify_movie'))
    return render_template('movies/movie_id.html')

# Route to modify movie by id -> localhost:5001/pelicula/modify/<int:id>
@pelicula_blueprint.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modify_movie_id(id):
    movie = Peliculas.query.get(id)
    if not movie:
        return render_template('movies/movie_not_found.html')
    if request.method == 'GET':
        return render_template('movies/movie_modify.html', movie=movie)
    elif request.method == 'POST':
        movie.nombre = request.form.get('nombre')
        movie.genero = request.form.get('genero')
        movie.duracion = request.form.get('duracion')
        movie.inventario = request.form.get('inventario')
        if not movie.nombre:
            flash('Oops! Movie name is missing', 'error')
            return render_template('movies/movie_modify.html', movie=movie)
        # Convert duration and inventory to int if provided
        movie.duracion = int(movie.duracion) if movie.duracion else None
        movie.inventario = int(movie.inventario) if movie.inventario else 1
        try:
            db.session.commit()
            flash('Movie modified successfully.', 'success')
            return redirect(url_for('pelicula.view_movies'))
        except Exception as e:
            db.session.rollback()
            flash('Error modifying movie. Details: {}'.format(str(e)), 'error')
            return redirect(url_for('pelicula.modify_movie_id', id=id))

# Route to delete movie -> localhost:5001/pelicula/eliminar
@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def delete_movie():
    if request.method == 'POST':
        movie_id = request.form.get('id_pelicula')
        try:
            movie_id = int(movie_id)
            return redirect(url_for('pelicula.delete_movie_id', id=movie_id))
        except ValueError:
            flash('Oops! Invalid ID, please enter a valid ID again', 'error')
    return render_template('movies/movie_id.html')

# Route to delete movie by id -> localhost:5001/pelicula/eliminar/<int:id>
@pelicula_blueprint.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def delete_movie_id(id):
    movie = Peliculas.query.get(id)
    if not movie:
        return render_template('movies/movie_not_found.html')
    else:
        rents = Rentar.query.filter_by(idPelicula=movie.idPelicula).all()
        if rents:
            flash('It is not possible to delete the movie because it has associated rentals', 'error')
        else:
            try:
                db.session.delete(movie)
                db.session.commit()
                flash('The movie was deleted successfully', 'success')
            except Exception as e:
                db.session.rollback()
                flash('Error deleting movie. Details: {}'.format(str(e)), 'error')
        return redirect(url_for('pelicula.view_movies'))
