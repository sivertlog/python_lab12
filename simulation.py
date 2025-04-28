from solar_system import SolarSystem

class Simulation:
    def __init__(self, solar_system: SolarSystem, width: int, height: int, num_periods: int):
        self._solar_system = solar_system
        self._width = width
        self._height = height
        self._num_periods = num_periods

    def run(self):
        for _ in range(self._num_periods):
            self._solar_system.move_planets()
            self._solar_system.show_planets()