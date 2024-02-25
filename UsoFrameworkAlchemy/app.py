from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelos.usuario import Base as BaseUsuario, Usuario
from modelos.pelicula import Base as BasePelicula, Pelicula
from modelos.renta import Base as BaseRenta, Renta
from sqlalchemy.exc import SQLAlchemyError
from tabulate import tabulate
from sqlalchemy import inspect

engine = create_engine('mysql+pymysql://lab:Developer123!@localhost/lab_ing_software')
BaseUsuario.metadata.create_all(engine)
BasePelicula.metadata.create_all(engine)
BaseRenta.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def ver_registros(tabla):
    try:
        columnas = [columna.key for columna in tabla.__table__.columns]
        registros = session.query(*[getattr(tabla, columna) for columna in columnas]).all()
        registros_data = [{columna: getattr(registro, columna) for columna in columnas} for registro in registros]
        if registros_data:
            print(tabulate(registros_data, headers="keys", tablefmt="pretty"))
        else:
            print("No hay registros en la tabla.")
    except SQLAlchemyError as e:
        print("Error al intentar obtener los registros:", e)

def filtrar_por_id(tabla, id):
    try:
        if tabla == Usuario:
            registro = session.query(tabla).filter_by(idUsuario=id).first()
        elif tabla == Pelicula:
            registro = session.query(tabla).filter_by(idPelicula=id).first()
        elif tabla == Renta:
            registro = session.query(tabla).filter_by(idRentar=id).first()  # Corregir aquí
        else:
            print("Tabla no válida.")
            return

        if registro:
            # Seleccionar las columnas relevantes para mostrar
            if tabla == Usuario:
                datos = {
                    'idUsuario': registro.idUsuario,
                    'nombre': registro.nombre,
                    'apPat': registro.apPat,
                    'apMat': registro.apMat,
                    'email': registro.email,
                    'password': registro.password
                }
            elif tabla == Pelicula:
                datos = {
                    'idPelicula': registro.idPelicula,
                    'nombre': registro.nombre,
                    'genero': registro.genero,
                    'duracion': registro.duracion,
                    'inventario': registro.inventario
                }
            elif tabla == Renta:
                datos = {
                    'idRentar': registro.idRentar,
                    'idUsuario': registro.idUsuario,
                    'idPelicula': registro.idPelicula,
                    'fecha_renta': registro.fecha_renta,
                    'dias_de_renta': registro.dias_de_renta,
                    'estatus': registro.estatus
                }

            # Imprimir los datos en forma de tabla
            print(tabulate([datos], headers="keys", tablefmt="pretty"))
        else:
            print("No se encontró ningún registro con ese ID.")
    except SQLAlchemyError as e:
        print("Error al intentar filtrar por ID:", e)




def actualizar_fecha_renta(id_renta, nueva_fecha):
    try:
        renta = session.query(Renta).filter_by(id=id_renta).first()
        if renta:
            renta.fecha_renta = nueva_fecha
            session.commit()
            print("Fecha de renta actualizada exitosamente.")
        else:
            print("No se encontró ninguna renta con ese ID.")
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al intentar actualizar la fecha de renta:", e)

def eliminar_registro(tabla, id=None):
    try:
        if id:
            registro = session.query(tabla).filter_by(id=id).first()
            if registro:
                session.delete(registro)
                session.commit()
                print("Registro eliminado exitosamente.")
            else:
                print("No se encontró ningún registro con ese ID.")
        else:
            session.query(tabla).delete()
            session.commit()
            print("Todos los registros de la tabla han sido eliminados.")
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al intentar eliminar el registro:", e)

if __name__ == "__main__":
    while True:
        print("\nMenú:")
        print("1. Ver registros de una tabla.")
        print("2. Filtrar registros por ID.")
        print("3. Actualizar fecha de renta de una película.")
        print("4. Eliminar un registro.")
        print("5. Salir.")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == "1":
            tabla = input("Ingrese el nombre de la tabla (Usuario, Pelicula, Renta): ")
            if tabla in ["Usuario", "Pelicula", "Renta"]:
                ver_registros(eval(tabla))
            else:
                print("Nombre de tabla no válido.")
        elif opcion == "2":
            tabla = input("Ingrese el nombre de la tabla (Usuario, Pelicula, Renta): ")
            if tabla in ["Usuario", "Pelicula", "Renta"]:
                id = input("Ingrese el ID del registro que desea filtrar: ")
                try:
                    id = int(id)
                    filtrar_por_id(eval(tabla), id)
                except ValueError:
                    print("ID inválido. Debe ser un número entero.")
            else:
                print("Nombre de tabla no válido.")
        elif opcion == "3":
            id_renta = input("Ingrese el ID de la renta que desea actualizar: ")
            nueva_fecha = input("Ingrese la nueva fecha de renta (YYYY-MM-DD): ")
            try:
                id_renta = int(id_renta)
                actualizar_fecha_renta(id_renta, nueva_fecha)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == "4":
            tabla = input("Ingrese el nombre de la tabla (Usuario, Pelicula, Renta): ")
            if tabla in ["Usuario", "Pelicula", "Renta"]:
                id = input("Ingrese el ID del registro que desea eliminar (deje en blanco para eliminar todos los registros): ")
                try:
                    if id:
                        id = int(id)
                    eliminar_registro(eval(tabla), id)
                except ValueError:
                    print("ID inválido. Debe ser un número entero.")
            else:
                print("Nombre de tabla no válido.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
