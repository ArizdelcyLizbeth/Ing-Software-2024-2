import { NavLink, Outlet } from "react-router-dom";
import '../CSS/Category.css'

export function Movies() {
  return (
    <>
      <h1>Movies</h1>
      <div className="card-container">
        <div className="card">
          <NavLink to='create'>Registrar una película</NavLink>
        </div>
        <div className="card">
          <NavLink to='read'>Nuestras películas</NavLink>
        </div>
        <div className="card">
          <NavLink to='update'>Actualizar una película</NavLink>
        </div>
        <div className="card">
          <NavLink to='delete'>Eliminar una película</NavLink>
        </div>

      </div>
      <div>
        <Outlet/>
      </div>
    </>
  );
}