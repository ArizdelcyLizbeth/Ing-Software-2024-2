import { rentas } from "../../../../../Data";
import '../../../CSS/Read.css';
import './ReadRent.css'; 
import { useNavigate } from "react-router-dom";

export default function ReadRents() {
    const navigate = useNavigate();

    const handleEdit = (rentId) => {
        navigate(`/rents/${rentId}`);
    };

    const isTimedOut = (renta) => {
        let rentDate = new Date(renta.fecha_renta);
        let today = new Date();
        let diff = today - rentDate;
        let days = Math.floor(diff / (1000 * 60 * 60 * 24));
        return days > renta.dias_de_renta;
    };

    return (
        <div>
            <h1>Rentas</h1> {/* Cambiado a "Rentas" */}
            {rentas && rentas.length > 0 ? (
                <table>
                    <thead>
                        <tr>
                            <th>Id</th>
                            <th>Usuario</th> {/* Cambiado a "Usuario" */}
                            <th>Película</th> {/* Cambiado a "Película" */}
                            <th>Fecha de Renta</th> {/* Cambiado a "Fecha de Renta" */}
                            <th>Días Rentados</th> {/* Cambiado a "Días Rentados" */}
                            <th>Estado</th> {/* Cambiado a "Estado" */}
                        </tr>
                    </thead>
                    <tbody>
                        {rentas.map((renta) => {
                            return (
                                <tr key={renta.idRentar} className={renta.estatus == 0 && isTimedOut(renta) ? 'timedout' : ''}>
                                    <td>{renta.idRentar}</td>
                                    <td>{renta.idUsuario}</td>
                                    <td>{renta.idPelicula}</td>
                                    <td>{renta.fecha_renta.toUTCString()}</td>
                                    <td>{renta.dias_de_renta}</td>
                                    <td>{renta.estatus == 1 ? 'Devuelta' : 'No devuelta'}</td> {/* Cambiado a "Devuelta" y "No devuelta" */}
                                    <td>
                                        <button onClick={() => handleEdit(renta.idRentar)}>Editar</button> {/* Cambiado a "Editar" */}
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            ) : (
                <h2>No hay rentas</h2> 
            )}
        </div>
    );
}
