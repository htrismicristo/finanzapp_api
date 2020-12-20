from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creando Motor y Conexion con la Base de Datos
SQLALCHEMY_DATABASE_URL = "postgres://sfodbpojxombnd:@ec2-52-6-75-198.compute-1.amazonaws.com:5432/d56asiq1bveijh"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:@localhost:5432/MISION_TIC"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creacion de la Sesión
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Creando Base para la creacion de los modelos
Base = declarative_base()
Base.metadata.schema = "finanzapp_db"
