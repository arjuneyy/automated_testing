from sqlalchemy import Column, String, Integer
from core.db import Base


class Account(Base):
    __tablename__ = 'tb_account'
    id = Column(Integer, primary_key=True)
    account_username = Column(String)
    account_password = Column(String)
    account_employee = Column(String)
    account_access_level = Column(Integer)

    def __init__(self, username: str,
                 password: str,
                 access_level: int,
                 employee: str = None) -> None:
        self.account_username = username
        self.account_password = password
        self.account_employee = employee
        self.account_access_level = access_level
