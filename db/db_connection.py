from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creando Motor y Conexion con la Base de Datos
SQLALCHEMY_DATABASE_URL = "postgresql://sfodbpojxombnd:6a2295d8561d7c1abe2c1aa6d400be2135c05d255e5a37620ad3d8f0d26a5634@ec2-52-6-75-198.compute-1.amazonaws.com:5432/d56asiq1bveijh"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:ds4biz23@localhost:5432/MISION_TIC"
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
