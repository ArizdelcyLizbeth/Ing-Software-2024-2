from Script1_PyMySQL import *


def punto1():
    connection = conectar_base_datos()
    insertar_registro_usuario(connection)

def punto2(): 
    connection = conectar_base_datos()
    insertar_registro_pelicula(connection)
    
def punto3():
    connection = conectar_base_datos()
    insertar_registro_usuario(connection)
    insertar_registro_pelicula(connection)

    with connection.cursor() as cursor:
        cursor.execute("SELECT idUsuario FROM usuarios WHERE email = %s", ('juan@example.com',))
        id_usuario = cursor.fetchone()[0]

    with connection.cursor() as cursor:
        cursor.execute("SELECT idPelicula FROM peliculas WHERE nombre = %s", ('Pelicula 1',))
        id_pelicula = cursor.fetchone()[0]

    insertar_registro_renta(id_usuario, id_pelicula, connection)

def punto4():
    connection = conectar_base_datos()
    filtrar_usuarios_por_apellido('ez', connection)  

if __name__ == '__main__':
    punto1()
    punto2()
    punto3()
    punto4()