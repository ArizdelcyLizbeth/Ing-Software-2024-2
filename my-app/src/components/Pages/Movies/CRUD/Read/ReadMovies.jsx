import { peliculas } from '../../../../../Data'
import '../../../CSS/Read.css'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'
import Card from '../../../../ConfirmationCard/Card'
import { deleteMovie } from '../../../../../DataFunctions'

export default function ReadMovies(){

    const navigate = useNavigate()
    const [confirm, setConfirm] = useState(false)
    const [movieId, setMovieId] = useState(0)

    const handleEdit = (movieId) => {
        navigate(`/movies/${movieId}`)
    }

    const handleDelete = (movieId) => {
        setMovieId(movieId)
        setConfirm(true)
    }

    const handleConfirm = () => {
        deleteMovie(movieId)
        setConfirm(false)
    }

    const handleCancel = () => {
        setConfirm(false)
        alert('Eliminación cancelada')
    }

    return(
        <div>
            <h1>Películas</h1>
            {peliculas && peliculas.length >0 ? 
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                            <th>Género</th>
                            <th>Duración</th>
                            <th>Inventario</th>
                        </tr>
                    </thead>
                    <tbody>
                        {peliculas.map((pelicula) => {
                            return(
                                <tr key={pelicula.idPelicula}>
                                    <td>{pelicula.idPelicula}</td>
                                    <td>{pelicula.nombre}</td>
                                    <td>{pelicula.genero}</td>
                                    <td>{pelicula.duracion}</td>
                                    <td>{pelicula.inventario}</td>
                                    <td>
                                        <button onClick={() => handleEdit(pelicula.idPelicula)}>Editar</button>
                                        <button onClick={() => handleDelete(pelicula.idPelicula)}>Eliminar</button>
                                    </td>
                                </tr>
                            ) }
                        )}
                    </tbody>
                </table> : <h2>No hay películas</h2>
            }
            {confirm && <Card message='¿Estás seguro de que quieres eliminar esta película?' handleConfirm={handleConfirm} handleCancel={handleCancel}/>}
        </div>
    )
}