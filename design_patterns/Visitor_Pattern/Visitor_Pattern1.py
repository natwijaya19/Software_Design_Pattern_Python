from __future__ import annotations

"""
Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.
"""

from abc import ABC, abstractmethod
from typing import List


# create component class interface
class ComponentInterface(ABC):
    """
    The Component interface declares an `accept` method that should take the
    base visitor interface as an argument.
    """

    @abstractmethod
    def accept(self, visitor: VisitorInterface) -> None:
        """
        Accept the visitor
        """
        pass


# create concrete component class
class ConcreteComponentA(ComponentInterface):
    """
    Each Concrete Component must implement the `accept` method in such a way
    that it calls the visitor's method corresponding to the component's class.
    """

    def accept(self, visitor_object: VisitorInterface) -> None:
        """
        Note that we're calling `visitConcreteComponentA`, which matches the
        current class name. This way we let the visitor know the class of the
        component it works with.

        - param visitor_object:
        - return:None
        """

        visitor_object.visit_concrete_component_a(self)

    @staticmethod
    def exclusive_method_of_concrete_component_a() -> str:
        """
        Concrete Components may have special methods that don't exist in their
        base class or interface. The Visitor is still able to use these methods
        since it's aware of the component's concrete class.
        :return: str
        """
        return "A"


class ConcreteComponentB:
    """
    Same here: visitConcreteComponentB => ConcreteComponentB
    """

    def accept(self, visitor_object: VisitorInterface) -> None:
        visitor_object.visit_concrete_component_b(self)

    @staticmethod
    def exclusive_method_of_concrete_component_b() -> str:
        return "B"


# create visitor class interface
class VisitorInterface(ABC):
    """
    The Visitor Interface declares a set of visiting methods that correspond to
    component classes. The signature of a visiting method allows the visitor to
    identify the exact class of the component that it's dealing with.
    """

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        """
        Visit concrete component A
        """
        pass

    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        """
        Visit concrete component B
        """
        pass


"""
Concrete Visitors implement several versions of the same algorithm, which can
work with all concrete component classes.

You can experience the biggest benefit of the Visitor pattern when using it with
a complex object structure, such as a Composite tree. In this case, it might be
helpful to store some intermediate state of the algorithm while executing
visitor's methods over various objects of the structure.
"""


# create concrete visitor classes
class ConcreteVisitor1(VisitorInterface):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.exclusive_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(VisitorInterface):
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        print(f"{element.exclusive_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components_list: List[ComponentInterface], visitor: VisitorInterface) -> None:
    """
    The client code can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    - param components_list:
    - param visitor:
    - return: None
    """
    for component in components_list:
        component.accept(visitor)

    # ...


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]
    print("The client code works with all visitors via the base VisitorInterface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)
    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
