import '../../../CSS/Create.css'
import { useParams } from "react-router-dom"
import { isUserRegistered, editUser } from "../../../../../DataFunctions"

export default function DetalleUsuario(){
    const params = useParams()

    const id = parseInt(params.userId)
    const usuario = isUserRegistered(id)

    const handleSubmit = (e) => {
        e.preventDefault()
        editUser(id, e.target.name.value, e.target.apPat.value, e.target.apMat.value, e.target.password.value, e.target.email.value, e.target.superUser.checked ? 1 : 0)
    }

    return (
        <div>
            <h1>Detalle de Usuario</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Nombre</label>
                <input type="text" id="name" name="name" defaultValue={usuario.nombre} required/>
                <label htmlFor="apPat">Apellido Paterno</label>
                <input type="text" id="apPat" name="apPat" defaultValue={usuario.apPat} required/>
                <label htmlFor="apMat">Apellido Materno</label>
                <input type="text" id="apMat" name="apMat" defaultValue={usuario.apMat} required/><br />
                <label htmlFor="email">Correo Electrónico</label>
                <input type="email" id="email" name="email" defaultValue={usuario.email} required/>
                <label htmlFor="password">Contraseña</label>
                <input type="password" id="password" name="password" defaultValue={usuario.password} required/>
                <label htmlFor="superUser">Super Usuario</label>
                <input type="checkbox" id="superUser" name="superUser" defaultChecked={usuario.superUser===1}/>
                <button type="submit">Editar</button>
            </form>
        </div>
    )
}
