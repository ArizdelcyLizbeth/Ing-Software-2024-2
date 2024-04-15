import '../../../CSS/Create.css';
import { createRent } from '../../../../../DataFunctions';

export default function CreateRent() {
    const handleSubmit = (e) => {
        e.preventDefault();
        createRent(e.target.idUsuario.value, e.target.idPelicula.value, e.target.fechaRenta.value, e.target.days.value, e.target.status.checked ? 1 : 0);
    };

    return (
        <div>
            <h1>Crear Renta</h1> {/* Cambiado a "Crear Renta" */}
            <form onSubmit={handleSubmit}>
                <label htmlFor="idUsuario">ID de Usuario</label> {/* Cambiado a "ID de Usuario" */}
                <input type="number" id="idUsuario" name="idUsuario" required />
                <label htmlFor="idPelicula">ID de Película</label> {/* Cambiado a "ID de Película" */}
                <input type="number" id="idPelicula" name="idPelicula" required />
                <label htmlFor="fechaRenta">Fecha de Renta</label> {/* Cambiado a "Fecha de Renta" */}
                <input type="date" id="fechaRenta" name="fechaRenta" required />
                <label htmlFor="days">Días de Renta</label> {/* Cambiado a "Días de Renta" */}
                <input type="number" id="days" name="days" required />
                <label htmlFor="status">Devuelta</label> {/* Cambiado a "Devuelta" */}
                <input type="checkbox" id="status" name="status" />
                <button type="submit">Registrar Renta</button> {/* Cambiado a "Registrar Renta" */}
            </form>
        </div>
    );
}
