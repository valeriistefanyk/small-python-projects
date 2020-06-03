from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implemention(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementionA(Implemention):
    def operation_implementation(self) -> str:
        return "ConcreteImplementionA: here's the result on the platform A."


class ConcreteImplementionB(Implemention):
    def operation_implementation(self) -> str:
        return "ConcreteImplementionB: here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end='')


if __name__ == "__main__":
    implementation = ConcreteImplementionA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print('\n')

    implementation = ConcreteImplementionB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
