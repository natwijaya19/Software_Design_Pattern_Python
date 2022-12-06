from __future__ import annotations

"""
In code, we can model a lightbulb using a class. 
We then could model the switch to control the behavior of a lightbulb. 
If the switch is flipped on or pressed, we expect an action to be sent to the lightbulb.

create an instance of Lightbulb named hueBulb. 
We then create an instance of the PowerSwitch object called switch 
and pass in the hueBulb instance.

The PowerSwitch class has a press method that will send a message to the lightbulb
to turn on or off depending on the state of the switch.
"""

from abc import ABC, abstractmethod
class Switchable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass



class LightBulb(Switchable):
      """
        The LightBulb class is a concrete implementation of the Switchable interface.
      """
      @staticmethod
      def turn_on() -> None:
          print("LightBulb: Bulb turned on...")

      @staticmethod
      def turn_off()-> None:
          print("LightBulb: Bulb turned off...")


class PowerSwitch:
        """
            The PowerSwitch class is a concrete implementation of the Switchable interface.
        """
        def __init__(self, switchable_instance: Switchable) -> None:
            self.switchable_obj = switchable_instance
            self.on = False

        def press(self) -> None:
            if self.on:
                self.switchable_obj.turn_off()
                self.on = False
            else:
                self.switchable_obj.turn_on()
                self.on = True

class Fan (Switchable):
    @staticmethod
    def turn_on() -> None:
        print("Fan: Fan turned on...")

    @staticmethod
    def turn_off()-> None:
        print("Fan: Fan turned off...")


if __name__ == "__main__":

    # press the power switch of lightbulb
    hue_bulb = LightBulb()
    power_switch = PowerSwitch(hue_bulb)
    power_switch.press()
    power_switch.press()
    power_switch.press()
    power_switch.press()

    # press the power switch of fan
    fan = Fan()
    power_switch = PowerSwitch(fan)
    power_switch.press()
    power_switch.press()
    power_switch.press()
    power_switch.press()
