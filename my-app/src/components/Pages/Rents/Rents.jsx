import { NavLink, Outlet } from "react-router-dom";
import '../CSS/Category.css';

export default function Rents() {
    return (
        <>
            <h1>Rentas</h1> {/* Cambiado a "Rentas" */}
            <div className="card-container">
                <div className="card">
                    <NavLink to='create'>Registrar una renta</NavLink> {/* Cambiado a "Registrar una renta" */}
                </div>
                <div className="card">
                    <NavLink to='read'>Nuestras rentas</NavLink> {/* Cambiado a "Nuestras rentas" */}
                </div>
                <div className="card">
                    <NavLink to='update'>Actualizar una renta</NavLink> {/* Cambiado a "Actualizar una renta" */}
                </div>
            </div>
            <div>
                <Outlet />
            </div>
        </>
    );
}
