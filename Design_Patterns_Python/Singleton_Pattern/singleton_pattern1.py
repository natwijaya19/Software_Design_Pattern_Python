from __future__ import annotations

"""
Singleton is a creational design pattern, which ensures that only one object of its kind exists
and provides a single point of access to it for any other code.

Singleton has almost the same pros and cons as global variables. 
Although they’re super-handy, they break the modularity of your code.

You can’t just use a class that depends on a Singleton in some other context, 
without carrying over the Singleton to the other context. 
Most of the time, this limitation comes up during the creation of unit tests.

"""

class SingletonMeta(type):
    """
    The SingletonMeta class is a metaclass that creates a Singleton base class when called

    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs) -> SingletonMeta:
        """
        This method is called each time a Singleton class is instantiated.
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        :param args:
        :param kwargs:
        :return:
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    The Singleton class defines the `getInstance` method that lets clients access
    the unique singleton instance.
    """

    def some_business_logic(self) -> None:
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        # ...


if __name__ == "__main__":
    # the client code
    S1 = Singleton()
    S2 = Singleton()

    if id(S1) == id(S2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")



