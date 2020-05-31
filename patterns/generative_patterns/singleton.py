from typing import Optional


class SingletonMeta(type):
    """
    Реализация Одиночки на метаклассе.
    """

    _instance: Optional['Singleton'] = None

    def __call__(self) -> 'Singleton':
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):
    """
    Любой одиночка должен содержать некоторую бизнес-логику,
    которая может быть выполнена на его экземпряре.
    """

    def some_business_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print('Singleton works!')
    print('id s1:', id(s1))
    print('id s2:', id(s2))
