from typing import List, Optional
from core.db.engine import DatabaseConnection
from core.db.models import Account
from sqlalchemy import exc


class UserAccountUtil:

    def __init__(self) -> None:
        self._db = DatabaseConnection()

    def filter_by_access_level(self, access_level: int) -> List[Account]:
        session = self._db.create_session()
        accounts: List[Account] = session.query(Account)\
            .filter(Account.account_access_level == access_level)\
            .all()
        session.close()

        return accounts

    def filter_by_(self, **kwargs) -> List[Account]:  # type: ignore
        session = self._db.create_session()
        query = session.query(Account)

        for attr, val in kwargs.items():
            query = query.filter(getattr(Account, attr) == val)

        accounts: List[Account] = query.all()
        session.close()

        return accounts

    def filter_by_like_(self, **kwargs) -> List[Account]:  # type: ignore
        session = self._db.create_session()
        query = session.query(Account)

        for attr, val in kwargs.items():
            query = query.filter(getattr(Account, attr).like(f'{val}%'))

        accounts: List[Account] = query.all()
        session.close()

        return accounts

    def filter_by_id(self, id: int) -> Optional[Account]:
        account: Account = None
        session = self._db.create_session()

        try:
            account = session.query(Account)\
                .filter(Account.id == id)\
                .one()
            session.close()
        except exc.NoResultFound:
            pass
        finally:
            session.close()

        return account

    def create_account(self, username: str,
                       password: str,
                       access_level: int,
                       employee: str = None) -> None:
        session = self._db.create_session()
        account = Account(username, password, access_level, employee)
        session.add(account)
        session.commit()
        session.close()

    def delete(self, *accounts: Account) -> None:
        session = self._db.create_session()
        try:
            for account in accounts:
                session.delete(account)
            session.commit()
        except:  # noqa
            session.rollback()
        finally:
            session.close()

    def delete_test_users(self, prefix: str = 'at_test') -> None:
        accounts = self.filter_by_like_(account_username=prefix)
        self.delete(*accounts)
