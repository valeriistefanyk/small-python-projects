"""
Порождающий паттерн Абстрактная фабрика
"""
from abc import ABC, abstractmethod


class Product(ABC):
    """ Интерфейс Продукта обьявляет операции, которые
        должны выполнить все конкретные продукты
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self):
        return 'concrete product a'


class ConcreteProduct2(Product):
    def operation(self):
        return 'concrete product b'


class Creator(ABC):
    """ Класс Создатель обьявляет фабричный метод, который
        должен возвращать обьект класса Продукт.
        Подклассы Создателя обычно предоставляют реализацию
        этого метода.
    """

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked \
            with {product.operation()}"
        return result


class ConcreteCreatorA(Creator):

    def factory_method(self) -> ConcreteProduct1:
        return ConcreteProduct1()


class ConcreteCreatorB(Creator):

    def factory_method(self) -> ConcreteProduct2:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    print("Client: I'm not aware of the creator's class, but it still works.")
    print(f"{creator.some_operation()}", end='')


if __name__ == "__main__":
    print('App: Launched with the ConcreteCreator1.')
    client_code(ConcreteCreatorA())
    print('\n')
