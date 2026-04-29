from sqlmodel import SQLModel, create_engine, Session


sqllite_file_name = "C:/Users/elem2/lab_2026/app/data/database.db"
sqlite_url = f"sqlite:///{sqllite_file_name}"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False},
                       echo=True
                       )


def init_database():
    SQLModel.metadata.create_all(engine)
