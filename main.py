from pickup_data.config import engine
from pickup_data.create_tables import insert_data

if __name__ == '__main__':
    insert_data(engine)
