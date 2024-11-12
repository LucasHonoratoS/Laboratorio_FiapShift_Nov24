from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão para o PostgreSQL
DATABASE_URL = "postgresql://livraria_wsmb_user:d2ZOCFaENDtxZGlufywQJmrJlN8s9h8Z@dpg-csptg5rqf0us73e887g0-a.oregon-postgres.render.com:5432/livraria_wsmb"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("Conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()