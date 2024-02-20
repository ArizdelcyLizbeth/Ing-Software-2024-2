import pymysql

def conectar_base_datos():
    return pymysql.connect(
        host='localhost',
        user='lab',
        password='Developer123!',
        database='lab_ing_software'
    )

def verificar_usuario_existente(email, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", (email,))
        count = cursor.fetchone()[0]
        return count > 0

def insertar_registro_usuario(connection):
    if not verificar_usuario_existente('juan@example.com', connection):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO usuarios (nombre, apPat, apMat, password, email) VALUES (%s, %s, %s, %s, %s)",
                           ('Juan', 'Perez', 'Gomez', 'password123', 'juan@example.com'))
        connection.commit()

def verificar_pelicula_existente(nombre, genero, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT idPelicula FROM peliculas WHERE nombre = %s AND genero = %s", (nombre, genero))
        result = cursor.fetchone()
        return result is not None

def insertar_registro_pelicula(connection):
    if not verificar_pelicula_existente('Pelicula 1', 'Drama', connection):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)",
                           ('Pelicula 1', 'Drama', 120, 10))
        connection.commit()

def verificar_renta_existente(id_usuario, id_pelicula, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM rentar WHERE idUsuario = %s AND idPelicula = %s", (id_usuario, id_pelicula))
        count = cursor.fetchone()[0]
        return count > 0

def insertar_registro_renta(id_usuario, id_pelicula, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM rentar WHERE idUsuario = %s AND idPelicula = %s", (id_usuario, id_pelicula))
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)",
                           (id_usuario, id_pelicula, '2024-02-18', 7, 1))
    connection.commit()

def filtrar_usuarios_por_apellido(apellido, connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE apPat LIKE %s", ('%' + apellido,))
        result = cursor.fetchall()
        for row in result:
            print(row)

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero, connection):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE peliculas SET genero = %s WHERE nombre = %s", (nuevo_genero, nombre_pelicula))
    connection.commit()

def eliminar_rentas_antiguas(connection):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM rentar WHERE fecha_renta <= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
    connection.commit()

def main():
    # Conectar a la base de datos
    connection = conectar_base_datos()

    # Ejecutar las funciones
    insertar_registro_usuario(connection)
    insertar_registro_pelicula(connection)
    
    # Obtener el ID de un usuario existente
    with connection.cursor() as cursor:
        cursor.execute("SELECT idUsuario FROM usuarios WHERE email = %s", ('juan@example.com',))
        id_usuario = cursor.fetchone()[0]

    # Obtener el ID de una película existente
    with connection.cursor() as cursor:
        cursor.execute("SELECT idPelicula FROM peliculas WHERE nombre = %s", ('Pelicula 1',))
        id_pelicula = cursor.fetchone()[0]

    insertar_registro_renta(id_usuario, id_pelicula, connection)
    cambiar_genero_pelicula('Pelicula 1', 'Comedia', connection)  # Cambiar el género de la película 'Pelicula 1'
    eliminar_rentas_antiguas(connection)  # Eliminar rentas antiguas
    filtrar_usuarios_por_apellido('ez', connection)  # Filtrar usuarios cuyo apellido termine en 'ez'

if __name__ == "__main__":
    main()