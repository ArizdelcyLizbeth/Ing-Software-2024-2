export let peliculas = [
  {idPelicula: 1, nombre: 'El Renacido', genero: 'Drama/Aventura', duracion: 156, inventario: 8},
  {idPelicula: 2, nombre: 'La La Land', genero: 'Musical/Romance', duracion: 128, inventario: 5},
  {idPelicula: 3, nombre: 'Mad Max: Fury Road', genero: 'Acción/Aventura', duracion: 120, inventario: 7},
  {idPelicula: 4, nombre: 'Inception', genero: 'Ciencia ficción/Acción', duracion: 148, inventario: 3},
  {idPelicula: 5, nombre: 'Coco', genero: 'Animación/Familiar', duracion: 105, inventario: 2},
  {idPelicula: 6, nombre: 'Mujer Maravilla', genero: 'Acción/Aventura', duracion: 141, inventario: 1},
  {idPelicula: 7, nombre: 'La Forma del Agua', genero: 'Fantasía/Drama', duracion: 123, inventario: 4},
  {idPelicula: 8, nombre: 'Logan', genero: 'Acción/Drama', duracion: 137, inventario: 6},
  {idPelicula: 9, nombre: 'Birdman', genero: 'Comedia/Drama', duracion: 119, inventario: 8},
  {idPelicula: 10, nombre: 'Spider-Man: Un nuevo universo', genero: 'Animación/Aventura', duracion: 117, inventario: 9}
]

export let usuarios = [
  {idUsuario: 1, nombre: 'Gabriel', apPat: 'Sánchez', apMat: 'García', password: 'abc123', email: 'gabriel@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 2, nombre: 'Lucía', apPat: 'Martínez', apMat: "Fernández", password: 'password', email: 'lucia@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 3, nombre: 'Jorge', apPat: 'Hernández', apMat: 'Díaz', password: 'qwerty', email: 'jorge@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 4, nombre: 'Valeria', apPat: 'López', apMat: 'Gómez', password: '123456', email: 'valeria@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 5, nombre: 'Diego', apPat: 'Pérez', apMat: 'Torres', password: 'contraseña', email: 'diego@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 6, nombre: 'Carolina', apPat: 'Gutiérrez', apMat: 'Santos', password: 'admin123', email: 'carolina@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 7, nombre: 'Mateo', apPat: 'Rodríguez', apMat: 'Ramírez', password: 'admin1234', email: 'mateo@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 8, nombre: 'Isabella', apPat: 'Fernández', apMat: 'Martín', password: '1234abcd', email: 'isabella@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 9, nombre: 'Sara', apPat: 'García', apMat: "Hernández", password: 'abcdef', email: 'sara@gmail.com', profilePicture: null, superUser: 0},
  {idUsuario: 10, nombre: 'Daniel', apPat: 'Martín', apMat: 'Sánchez', password: 'password123', email: 'daniel@gmail.com', profilePicture: null, superUser: 1}
]

export let rentas = [
  {idRentar: 1, idUsuario: 1, idPelicula: 1, fecha_renta: new Date(2023, 8, 10), dias_de_renta: 7, estatus: 0},
  {idRentar: 2, idUsuario: 2, idPelicula: 2, fecha_renta: new Date(2022, 12, 5), dias_de_renta: 5, estatus: 0},
  {idRentar: 3, idUsuario: 3, idPelicula: 3, fecha_renta: new Date(2021, 11, 11), dias_de_renta: 3, estatus: 0},
  {idRentar: 4, idUsuario: 4, idPelicula: 4, fecha_renta: new Date(2021, 30, 11), dias_de_renta: 4, estatus: 0},
  {idRentar: 5, idUsuario: 5, idPelicula: 5, fecha_renta: new Date(2021, 9, 1), dias_de_renta: 6, estatus: 0},
  {idRentar: 6, idUsuario: 6, idPelicula: 6, fecha_renta: new Date(2020, 7, 14), dias_de_renta: 8, estatus: 0},
  {idRentar: 7, idUsuario: 7, idPelicula: 7, fecha_renta: new Date(2019, 8, 22), dias_de_renta: 2, estatus: 0},
  {idRentar: 8, idUsuario: 8, idPelicula: 8, fecha_renta: new Date(2019, 2, 26), dias_de_renta: 1, estatus: 0},
  {idRentar: 9, idUsuario: 9, idPelicula: 9, fecha_renta: new Date(2024, 6, 20), dias_de_renta: 10, estatus: 0},
  {idRentar: 10, idUsuario: 10, idPelicula: 10, fecha_renta: new Date(2023, 3, 7), dias_de_renta: 9, estatus: 0}
]
