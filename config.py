from sqlalchemy import create_engine

engine = create_engine('postgresql://zucks:admin1@localhost:5432/zucks', echo=True)
