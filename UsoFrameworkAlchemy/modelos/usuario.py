from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True)  # Cambiar 'id' a 'idUsuario'
    nombre = Column(String)
    apPat = Column(String)
    apMat = Column(String)
    password = Column(String)
    email = Column(String, unique=True)

    
    @classmethod
    def filtrar_por_id(cls, session, id_usuario):
        return session.query(cls).filter_by(idUsuario=id_usuario).all()