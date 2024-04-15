import React from 'react';
import '../../../CSS/Create.css';
import { createUser } from '../../../../../DataFunctions';

export default function CreateUser() {
    const handleRegistrationSubmit = (e) => {
        e.preventDefault();
        const { name, apPat, apMat, password, email, superUser } = e.target;
        createUser(name.value, apPat.value, apMat.value, password.value, email.value, superUser.checked);
    };

    return (
        <div>
            <h1>Registrar Usuario</h1>
            <form onSubmit={handleRegistrationSubmit}>
                <label htmlFor="name">Nombre</label>
                <input type="text" id="name" name="name" required />
                <label htmlFor="apPat">Apellido Paterno</label>
                <input type="text" id="apPat" name="apPat" required />
                <label htmlFor="apMat">Apellido Materno</label>
                <input type="text" id="apMat" name="apMat" required />
                <label htmlFor="email">Correo Electrónico</label>
                <input type="email" id="email" name="email" required />
                <label htmlFor="password">Contraseña</label>
                <input type="password" id="password" name="password" required />
                <label htmlFor="superUser">Super Usuario</label>
                <input type="checkbox" id="superUser" name="superUser" />
                <button type="submit">Registrar</button>
            </form>
        </div>
    );
}
