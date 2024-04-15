import '../../../CSS/Create.css'
import { createMovie } from '../../../../../DataFunctions'
export default function CreateMovie(){

    const handleSubmit = (e) => {
        e.preventDefault()
        createMovie(e.target.title.value, e.target.genre.value, e.target.length.value, e.target.stock.value)
    }

    return(
        <div>
            <h1>Registrar una película</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="title">Título</label>
                <input type="text" id="title" name="title" required/>
                <label htmlFor="genre">Género</label>
                <input type="text" id="genre" name="genre" required/>
                <label htmlFor="length">Duración (minutos)</label>
                <input type="number" id="length" name="length" required/>
                <label htmlFor="stock">Existencias</label>
                <input type='number' id="stock" name="stock" required/>
                <button type="submit">Registrar</button>
            </form>
        </div>
    )
}