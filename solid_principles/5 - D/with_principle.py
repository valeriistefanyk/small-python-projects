import abc

class Database(abc.ABC):
    @abc.abstractmethod
    def insert():
        pass

    @abc.abstractmethod
    def update():
        pass

    @abc.abstractmethod
    def delete():
        pass

class MySQLDatabase(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

class MongoDB(Database):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class BudgetReport:
    def __init__(self, database):
        self.database = database

    def open(self, date):
        pass

    def save(self):
        pass

if __name__ == "__main__":
    mysql = MySQLDatabase()
    budget = BudgetReport(mysql)