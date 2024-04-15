import { usuarios } from "../../../../../Data"
import '../../../CSS/Read.css'
import { useNavigate } from "react-router-dom"
import { deleteUser } from "../../../../../DataFunctions"
import { useState } from "react"
import Card from "../../../../ConfirmationCard/Card"

export default function ReadUsers(){

    const navigate = useNavigate()

    const [confirmar, setConfirmar] = useState(false)
    const [idUsuario, setIdUsuario] = useState(0)

    const manejarEdicion = (idUsuario) => {
        navigate(`/usuarios/${idUsuario}`)
    }

    const manejarEliminacion = (idUsuario) => {
        setIdUsuario(idUsuario)
        setConfirmar(true)
    }

    const confirmarEliminacion = () => {
        deleteUser(idUsuario)
        setConfirmar(false)
    }

    const cancelarEliminacion = () => {
        setConfirmar(false)
        alert('Eliminación cancelada')
    }

    return(
        <div>
            <h1>Usuarios</h1>
            {usuarios && usuarios.length > 0 ? 
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Nombre</th>
                            <th>Apellido Paterno</th>
                            <th>Apellido Materno</th>
                            <th>Email</th>
                            <th>Superusuario</th>
                        </tr>
                    </thead>
                    <tbody>
                        {usuarios.map((usuario) => {
                            return(
                                <tr key={usuario.idUsuario}>
                                    <td>{usuario.idUsuario}</td>
                                    <td>{usuario.nombre}</td>
                                    <td>{usuario.apPat}</td>
                                    <td>{usuario.apMat}</td>
                                    <td>{usuario.email}</td>
                                    <td>{usuario.superUsuario}</td>
                                    <td>
                                        <button onClick={() => manejarEdicion(usuario.idUsuario)}>Editar</button>
                                        <button onClick={() => manejarEliminacion(usuario.idUsuario)}>Eliminar</button>
                                    </td>
                                </tr>
                            ) }
                        )}
                    </tbody>
                </table> : <h2>No hay usuarios</h2>
            }
            {confirmar && <Card message='¿Estás seguro de que quieres eliminar este usuario?' handleConfirm={confirmarEliminacion} handleCancel={cancelarEliminacion}/>}
        </div>
    )
        
}
