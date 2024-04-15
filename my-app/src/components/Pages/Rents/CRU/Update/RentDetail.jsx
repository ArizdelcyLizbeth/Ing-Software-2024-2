import { useParams } from "react-router-dom"
import { editRent, isRentRegistered } from "../../../../../DataFunctions"

export default function DetalleRenta(){
    const params = useParams()

    const id = parseInt(params.idRenta)
    const renta = isRentRegistered(id)


    const handleSubmit = (e) => {
        e.preventDefault()
        editRent(id, e.target.status.checked ? 1 : 0)
    }

    return (
        <div>
            <h1>Detalles de la Renta</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="idUsuario">ID de Usuario</label>
                <p>{renta.idUsuario}</p>
                <label htmlFor="idPelicula">ID de Película</label>
                <p>{renta.idPelicula}</p>
                <label htmlFor="fechaRenta">Fecha de Renta</label>
                <p>{renta.fecha_renta.toUTCString()}</p>
                <label htmlFor="dias">Días de Renta</label>
                <p>{renta.dias_de_renta}</p>
                <label htmlFor="estado">Devuelta</label>
                <input type="checkbox" id="estado" name="estado"  defaultChecked={renta.devuelta === 1}/>
                <button type="submit">Actualizar Renta</button>
            </form>
        </div>
    )
}
