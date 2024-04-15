import './Navigation.css';
import { NavLink } from 'react-router-dom';

export default function Navigation() {
  return (
    <>
      <div id="sidebar">
        <div></div>
        <nav>
          <ul>
            <li>
              <NavLink to='/'>Home</NavLink>
              <img src="https://png.pngtree.com/png-clipart/20220303/original/pngtree-cartoon-cute-pink-round-background-film-projector-film-png-image_7386187.png" alt="Im" />
            </li>
            <li>
              <NavLink to='movies'>Movies</NavLink>
              <img src="https://jaimefariasinforma.com/wp-content/uploads/2023/06/Diseno-sin-titulo-97.jpg" alt="Movies Image" />
            </li>
            <li>
              <NavLink to='users'>Users</NavLink>
              <img src="https://images.vexels.com/media/users/3/135250/isolated/preview/f476f930e98bea4034f47b9dd713d128-icono-de-sombra-de-usuarios.png" alt="Users Image" />
            </li>
            <li>
              <NavLink to='rents'>Rents</NavLink>
              <img src="https://i.pinimg.com/originals/42/97/83/429783b5e349774bee8bcd4f8f11e14e.png" alt="Rents Image" />
            </li>
          </ul>
        </nav>
      </div>
    </>
  );
}
