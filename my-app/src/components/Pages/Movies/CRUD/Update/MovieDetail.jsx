import { useParams } from "react-router-dom"
import { isMovieRegistered, editMovie } from "../../../../../DataFunctions"

export default function DetallePelicula() {

    const params = useParams()
    const id = parseInt(params.movieId)

    const movie = isMovieRegistered(id)

    const handleSubmit = (e) => {
        e.preventDefault()
        editMovie(id, e.target.title.value, e.target.genre.value, e.target.length.value, e.target.stock.value)
    }

    return (
        <div>
            <h1>Detalle de la película</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="title">Título</label>
                <input type="text" id="title" name="title" required defaultValue={movie.nombre}/>
                <label htmlFor="genre">Género</label>
                <input type="text" id="genre" name="genre" required defaultValue={movie.genero}/>
                <label htmlFor="length">Duración (minutos)</label>
                <input type="number" id="length" name="length" required defaultValue={movie.duracion}/>
                <label htmlFor="stock">Inventario</label>
                <input type='number' id="stock" name="stock" required defaultValue={movie.inventario}/>
                <button type="submit">Actualizar</button>
            </form>
        </div>
    )
}
