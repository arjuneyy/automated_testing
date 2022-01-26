import os
import sqlalchemy as sa
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class IDatabaseConnection(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @property
    @abstractmethod
    def engine(self) -> Engine:
        pass

    @abstractmethod
    def create_session(self) -> sessionmaker:
        pass


class DatabaseConnection(IDatabaseConnection):

    def __init__(self) -> None:
        # Load environment variables
        load_dotenv()
        self._engine = self.create_engine()

    @property
    def engine(self) -> Engine:
        return self._engine

    def create_session(self) -> sessionmaker:
        return sessionmaker(bind=self._engine)()

    def create_engine(self) -> Engine:
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')

        driver = 'mysql+pymysql'
        database = f'{user}:{password}@{host}:{port}/{db_name}'

        return sa.create_engine(f'{driver}://{database}')

    def generate_metadata(self) -> None:
        Base.metadata.create_all(self._engine)
