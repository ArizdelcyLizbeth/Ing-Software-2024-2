import '../../../CSS/Update.css'
import { useState } from 'react'
import { deleteMovie } from '../../../../../DataFunctions'
import Card from '../../../../ConfirmationCard/Card.jsx'

export default function DeleteMovie(){
    const [confirm, setConfirm] = useState(false)
    const [movieId, setMovieId] = useState(0)


    const handleSubmit = (e) => {
        e.preventDefault()
        setMovieId(parseInt(e.target.movieId.value))
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
            <h1>Eliminar Película</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="movieId">ID de la Película</label>
                <input type="number" id="movieId" name="movieId" required/>
                <button type="submit">Eliminar</button>
            </form>

            {confirm &&
                <Card message='¿Estás seguro de que quieres eliminar esta película?' handleConfirm={handleConfirm} handleCancel={handleCancel}/>
            }

        </div>
    )
}