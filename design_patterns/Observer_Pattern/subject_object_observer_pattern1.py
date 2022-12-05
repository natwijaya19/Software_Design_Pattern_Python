from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

# create concrete_subject interface
class SubjectInterface(ABC):
    """Subject interface declare methods for managing observers from the client object"""

    def __init__(self):
        self.state = None

    @abstractmethod
    def attach(self, observer: ObserverInterface) -> None:
        """Attach an observer to the concrete_subject"""
        pass

    @abstractmethod
    def detach(self, observer: ObserverInterface) -> None:
        """Detach an observer from the concrete_subject"""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event"""
        pass

# create observer interface
class ObserverInterface(ABC):
    """ObserverInterface interface declare the update method, used by subjects"""

    @abstractmethod
    def update(self, concrete_subject: SubjectInterface) -> None:
        """Receive update from concrete_subject"""
        pass


# create concrete concrete_subject
class ConcreteSubjectInterface(SubjectInterface):
    """Concrete concrete_subject stores state of interest to ConcreteObserver objects"""

    state: int = None
    """For the sake of simplicity, the concrete_subject's state, essential to all subscribers, is stored in this variable"""

    _observers: List[ObserverInterface] = []
    """List of subscribers. In real life, the list of subscribers can be stored more comprehensively (categorized by event type, etc.)"""

    def attach(self, observer: ObserverInterface) -> None:
        """Attach an observer to the concrete_subject"""
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: ObserverInterface) -> None:
        """Detach an observer from the concrete_subject"""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Trigger an update in each subscriber"""
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self.state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self.state}")
        self.notify()

# create concrete observer A
class ConcreteObserverAInterface(ObserverInterface):
    """Concrete ObserverInterface A reacts to the updates issued by the Concrete Subject"""

    def update(self, concrete_subject: SubjectInterface) -> None:
        """

        type concrete_subject: SubjectInterface
        """
        if concrete_subject.state < 3:
            print("ConcreteObserverAInterface: Reacted to the event")


# create concrete observer B
class ConcreteObserverBInterface(ObserverInterface):
    """Concrete ObserverInterface B reacts to the updates issued by the Concrete Subject"""

    def update(self, concrete_subject: SubjectInterface) -> None:
        if concrete_subject.state == 0 or concrete_subject.state >= 2:
            print("ConcreteObserverBInterface: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubjectInterface()

    observer_a = ConcreteObserverAInterface()
    subject.attach(observer_a)

    observer_b = ConcreteObserverBInterface()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

