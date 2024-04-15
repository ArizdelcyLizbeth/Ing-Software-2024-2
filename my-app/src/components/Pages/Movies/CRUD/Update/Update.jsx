import '../../../CSS/Update.css'
import { useNavigate } from "react-router-dom"
import { isMovieRegistered } from "../../../../../DataFunctions"

export default function UpdateMovie(){

    const navigate = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        const movieId = parseInt(e.target.movieId.value)
        if(isMovieRegistered(movieId)){
            navigate(`/movies/${movieId}`)
            /*localStorage.setItem('movie', JSON.stringify(movie))
            window.location.href = '/movies/update/movieDetail'*/
        }else{
            alert('Película no encontrada')
        }
    }

    return(
        <div>
            <h1>Actualizar Película</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="movieId">Id de la Película</label>
                <input type="number" id="movieId" name="movieId" required/>
                <button type="submit">Buscar</button>
            </form>
        </div>
    )
}