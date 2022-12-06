from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

"""
Builder is a creational design pattern, which allows constructing complex objects step by step.

Unlike other creational patterns, Builder does not require products to have a common interface. 
That makes it possible to produce different products using the same construction process.
"""


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of the
    Product objects.
    """

    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass
class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide specific
    implementations of the building steps. Your program may have several variations
    of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder_instance instance should contain a blank product object, which is
        used in further assembly.
        """
        self._product = None
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    # All production steps work with the same product instance.
    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder_instance
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.

        return: Product1
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Product1:
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self)-> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder_instance: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        - param builder_instance:
        - return: None

        """
        self._builder = builder_instance


    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_minimal_viable_product(self)-> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self)-> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder_instance object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder_instance object.
    """
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("standard full featured product")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("custom product")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

