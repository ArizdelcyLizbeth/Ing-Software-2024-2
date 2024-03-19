from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class Peliculas(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer, default=1, nullable=False)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"<Peliculas(idPelicula='{self.idPelicula}', nombre='{self.nombre}', genero='{self.genero}', " \
                f"duracion={self.duracion}, inventario={self.inventario})>"