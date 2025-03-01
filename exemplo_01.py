from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print('Conexão com SQLite estabelecida.')

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

#Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# novo_usuario = Usuario(nome='João', idade='28')
# session.add(novo_usuario)
# session.commit()

# print('Usuário inserido com sucesso.')

# usuario = session.query(Usuario).filter_by(nome='João').first()
# print(f'Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}')

# try:
#     novo_usuario = Usuario(nome='Ana', idade=25)
#     session.add(novo_usuario)
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()

with Session() as session:
    novo_usuario = Usuario(nome='Rafael', idade=37)
    session.add(novo_usuario)