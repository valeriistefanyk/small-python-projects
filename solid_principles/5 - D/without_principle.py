""" 
высокоуровневый класс формирования бюджетных отчётов 
напрямую использует класс базы данных для загрузки и 
сохранения своей информации.
"""


class MySQLDatabase:
    
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class BudgetReport:
    # database = MySQLDatabase
    def __init__(self, database):
        self.database = database

    def open(self, data):
        pass

    def save(self):
        pass