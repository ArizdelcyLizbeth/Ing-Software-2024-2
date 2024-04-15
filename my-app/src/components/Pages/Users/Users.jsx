import React from "react";
import { NavLink, Outlet } from "react-router-dom";
import "../CSS/Category.css";

export default function Usuarios() {
    return (
        <>
            <h1>Usuarios</h1>
            <div className="card-container">
                <div className="card">
                    <NavLink to="create">Registrar un usuario</NavLink>
                </div>
                <div className="card">
                    <NavLink to="read">Nuestros usuarios</NavLink>
                </div>
                <div className="card">
                    <NavLink to="update">Actualizar un usuario</NavLink>
                </div>
                <div className="card">
                    <NavLink to="delete">Eliminar un usuario</NavLink>
                </div>
            </div>
            <div>
                <Outlet />
            </div>
        </>
    );
}
