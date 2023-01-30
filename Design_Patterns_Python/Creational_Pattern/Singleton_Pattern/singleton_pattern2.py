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

from threading import Lock, Thread

class SingletonMetha(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.

        Now, imagine that the program has just been launched. Since there's no
        Singleton instance yet, multiple threads can simultaneously pass the
        previous conditional and reach this point almost at the same time. The
        first of them will acquire lock and will proceed further, while the
        rest will wait here.
        """
        with cls._lock:
            """
            The first thread to acquire the lock, reaches this conditional,
            goes inside and creates the Singleton instance. Once it leaves the
            lock block, a thread that might have been waiting for the lock
            release may then enter this section. But since the Singleton field
            is already initialized, the thread won't create a new object.
            """
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMetha):

    value: str = None

    """
    We'll use this property to prove that our Singleton really works.

    The Singleton's constructor should always be private to prevent direct
    construction calls with the `new` operator.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self) -> None:
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        pass

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    # the client code
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, "
          "then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()

    process3 = Thread(target=test_singleton, args=("WOO",))
    process4 = Thread(target=test_singleton, args=("HOO",))
    process3.start()
    process4.start()



