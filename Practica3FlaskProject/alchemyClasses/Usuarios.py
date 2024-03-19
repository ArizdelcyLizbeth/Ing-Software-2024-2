from sqlalchemy import Column, Integer, String, LargeBinary, Boolean, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True)
    profilePicture = Column(LargeBinary)
    superUser = Column(Boolean, default=False)

    def __init__(self, nombre, apPat, apMat=None, password=None, email=None, superUser=False):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.superUser = superUser

    def __str__(self):
        return (f"<Usuarios(idUsuario='{self.idUsuario}', nombre='{self.nombre}', apPat='{self.apPat}', apMat='{self.apMat}', "
                f"password='{self.password}', email='{self.email}', superUser='{self.superUser}')>")