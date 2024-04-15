import '../../../CSS/Update.css'
import { useState } from 'react'
import { deleteUser } from '../../../../../DataFunctions'
import Card from '../../../../ConfirmationCard/Card.jsx'

export default function DeleteUser(){

    const [confirmar, setConfirmar] = useState(false)
    const [idUsuario, setIdUsuario] = useState(0)


    const manejarEnvio = (e) => {
        e.preventDefault()
        setIdUsuario(parseInt(e.target.idUsuario.value))
        setConfirmar(true)
    }

    const confirmarEliminar = () => {
        deleteUser(idUsuario)
        setConfirmar(false)
    }

    const cancelarEliminar = () => {
        setConfirmar(false)
        alert('Eliminación cancelada')
    }

    return(
        <div>
            <h1>Eliminar Usuario</h1>
            <form onSubmit={manejarEnvio}>
                <label htmlFor="idUsuario">ID de Usuario</label>
                <input type="number" id="idUsuario" name="idUsuario" required/>
                <button type="submit">Eliminar</button>
            </form>
            {confirmar && <Card message='¿Estás seguro de que quieres eliminar este usuario?' handleConfirm={confirmarEliminar} handleCancel={cancelarEliminar}/>}
        </div>
    )
}
