"""
*******************************************************************************
Strategy design pattern is a behavioral design pattern that lets you define
a family of algorithms, put each of them into a separate class, and make
their objects interchangeable.
*******************************************************************************
"""

from abc import ABC, abstractmethod


# *******************************************
# Strategy class
# The strategy interface declares operations common to all
# supported versions of some algorithm. The context uses this
# interface to call the algorithm defined by the concrete
# strategies.
# *******************************************
class Strategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int):
        pass


# // Concrete strategies implement the algorithm while following
# // the base strategy interface. The interface makes them
# // interchangeable in the context.
class ConcreteStrategyAdd(Strategy):
    def execute(self, a: int, b: int):
        add_result = a + b
        return add_result


class ConcreteStrategySubtract(Strategy):
    def execute(self, a: int, b: int):
        sub_result = a - b
        return sub_result


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a: int, b: int) -> int:
        mult_result: int = a * b
        return mult_result


# *******************************************
# Context class
# The context defines the interface of interest to clients.

# *******************************************
class Context:
    # // The context maintains a reference to one of the strategy
    #     // objects. The context doesn't know the concrete class of a
    #     // strategy. It should work with all strategies via the
    #     // strategy interface.
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, a: int, b: int) -> int:
        context_result: int = self._strategy.execute(a, b)
        return context_result


# client application
# // The client code picks a concrete strategy and passes it to
# // the context. The client should be aware of the differences
# // between strategies in order to make the right choice.
def main():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))

    print("\nPlease select from the following options:")
    print("Addition\t : 1")
    print("Subtraction\t : 2")
    print("Multiplication\t : 3")
    selected_strategy: int = int(input("Enter strategy number:"))

    context = Context()
    if selected_strategy == 1:
        concreteStrategyAdd = ConcreteStrategyAdd()
        context.set_strategy(concreteStrategyAdd)

    elif  selected_strategy == 2:
        concreteStrategySubtract = ConcreteStrategySubtract()
        context.set_strategy(concreteStrategySubtract)

    elif selected_strategy == 3:
        concreteStrategyMultiply = ConcreteStrategyMultiply()
        context.set_strategy(concreteStrategyMultiply)

    else:
        print("There no available execution for {}", selected_strategy)

    client_result = context.execute_strategy(a, b)
    print(client_result)


if __name__ == "__main__":
    main()
