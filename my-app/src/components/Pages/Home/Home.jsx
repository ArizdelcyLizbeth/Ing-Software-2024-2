import React from 'react';
import './Home.css';

export function Home() {
  return (
    <div className='home-container'>
      <div className='content'>
        <h1 className='title'>¡Bienvenido a ClonBuster!</h1>
        <p className='description'>Explora nuestro catálogo de películas y disfruta de la mejor experiencia cinematográfica.</p>
        <div className='image-container'>
          <img src='https://png.pngtree.com/png-clipart/20220303/original/pngtree-cartoon-cute-pink-round-background-film-projector-film-png-image_7386187.png' alt='Proyector de cine' className='image' />
        </div>
      </div>
    </div>
  );
}
