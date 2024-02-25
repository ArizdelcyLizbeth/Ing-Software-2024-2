from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Renta(Base):
    __tablename__ = 'rentar'

    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False, default=func.now())
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)

    @classmethod
    def filtrar_renta_por_id(cls, session, id_renta):
        try:
            renta = session.query(cls).filter_by(idRentar=id_renta).first()
            if renta:
                return renta
            else:
                print("No se encontró ninguna renta con ese ID.")
                return None
        except SQLAlchemyError as e:
            print("Error al intentar filtrar la renta por ID:", e)
            return None