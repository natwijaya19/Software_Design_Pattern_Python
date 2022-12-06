from __future__ import annotations

class LightBulb:
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
        def __init__(self, light_bulb: LightBulb) -> None:
            self.light_bulb = light_bulb
            self.on = False

        def press(self) -> None:
            if self.on:
                self.light_bulb.turn_off()
                self.on = False
            else:
                self.light_bulb.turn_on()
                self.on = True


if __name__ == "__main__":
    hue_bulb = LightBulb()
    power_switch = PowerSwitch(hue_bulb)
    power_switch.press()
    power_switch.press()

