import '../../../CSS/Update.css'
import { useNavigate } from "react-router-dom"
import { isUserRegistered } from "../../../../../DataFunctions"

export default function UpdateUser(){

    const navigate = useNavigate()

    const handleSubmit = (e) => {
        e.preventDefault()
        const idUsuario = parseInt(e.target.userId.value)
        if(isUserRegistered(idUsuario)){
            navigate(`/usuarios/${idUsuario}`)
        }else{
            alert('Usuario no encontrado')
        }
    }

    return(
        <div>
            <h1>Actualizar Usuario</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="userId">ID de Usuario</label>
                <input type="number" id="userId" name="userId" required/>
                <button type="submit">Buscar</button>
            </form>
        </div>
    )
}
