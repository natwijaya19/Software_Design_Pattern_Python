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


