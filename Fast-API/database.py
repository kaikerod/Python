# Arquivo para criar a conexão com o banco de dados
# sqlalchemy - Cria a conexão com o banco de dados SQL com Python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

# Conexão com o banco de dados PostgreSQL | define usuário, senha, host e nome do banco
#                             usuário/  senha/  host/     nome do banco
DATABASE_URL = "postgresql://postgres:123456@localhost/escola"

# Motor do banco de dados, comunica com o FastAPI
engine = create_engine(DATABASE_URL)

# Cria a sessão de conexão com o banco de dados
SessionLocal = sessionmaker(bind=engine)

# Cria a base para os modelos
Base = declarative_base()