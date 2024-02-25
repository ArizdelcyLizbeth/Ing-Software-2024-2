from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Pelicula(Base):
    __tablename__ = 'peliculas'
    
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String)
    genero = Column(String)
    duracion = Column(Integer)
    inventario = Column(Integer)

@classmethod
def filtrar_pelicula_por_id(cls, session, id_pelicula):
    try:
        pelicula = session.query(cls).filter_by(idPelicula=id_pelicula).first()
        if pelicula:
            return pelicula
        else:
            print("No se encontró ninguna película con ese ID.")
            return None
    except SQLAlchemyError as e:
        print("Error al intentar filtrar la película por ID:", e)
        return None
