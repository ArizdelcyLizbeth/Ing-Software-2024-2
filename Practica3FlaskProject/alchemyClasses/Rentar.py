from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from alchemyClasses import db
from datetime import datetime

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False, default=datetime.now)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)

    usuario = relationship("Usuarios", back_populates="rentas")
    pelicula = relationship("Peliculas", back_populates="rentas")

    def __init__(self, idUsuario, idPelicula, fecha_renta=None, dias_de_renta=5, estatus=False):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        if fecha_renta is not None:
            self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return (f"<Rentar(idRentar='{self.idRentar}', idUsuario='{self.idUsuario}', idPelicula='{self.idPelicula}', "
                f"fecha_renta='{self.fecha_renta}', dias_de_renta='{self.dias_de_renta}', estatus='{self.estatus}')>")