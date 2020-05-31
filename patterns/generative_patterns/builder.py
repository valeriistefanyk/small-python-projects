from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    """ Интерфейс Строителя обьявляет создающие методы
        для различных частей обьектов Продуктов
    """
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """ Классы конкретного Строителя следуют интерфейсу Строителя
        и предоставляют конкретные реализации шагов построения.
        Ваша программа может иметь несколько вариантов Строителей,
        реализованных по-разному.
    """
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> 'Product1':
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add('Part A1')

    def produce_part_b(self) -> None:
        self._product.add('Part B1')


class ConcreteBuilder2(Builder):
    """ Классы конкретного Строителя следуют интерфейсу Строителя
        и предоставляют конкретные реализации шагов построения.
        Ваша программа может иметь несколько вариантов Строителей,
        реализованных по-разному.
    """
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product2()

    @property
    def product(self) -> 'Product2':
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add('Part A2')

    def produce_part_b(self) -> None:
        self._product.add('Part B2')


class Product1():
    """ Имеет смысл использовать паттерн Строитель только тогда, когда
        ваши продукты достаточно сложны и требуют обширной конфигурации.

        В отличие от других порождающих паттернов, различные конкретные
        строители могут производить несвязанные продукты. Другими словами,
        результаты различных строителей могут не всегда следовать одному
        и тому же интерфейсу.
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Product2():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """ Директор отвечает только за выполнение шагов построения в
        определенной последовательности. Это полезно при производстве
        продуктов в определенном порядке или особой конфигурации. Строго
        говоря, класс Директор необязателен, так как клиент может
        напрямую управлять строителями.
    """
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()


if __name__ == "__main__":
    """ Клиентский код создает обьект-строитель, передает его директору, а
        затем инициирует процесс построения. Конечный результат извлекается
        из обьекта-строителя.
    """
    director = Director()
    builder = ConcreteBuilder2()
    director.builder = builder

    print("Standart basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print('\n')

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print('\n')

    # без использования Директора.
    print('Custom product: ')
    builder.produce_part_b()
    builder.produce_part_a()
    builder.product.list_parts()
