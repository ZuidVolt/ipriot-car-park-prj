from display import Display
from sensor import Sensor


class CarPark:
    def __init__(
        self,
        location: str | None,
        capacity: int,
        plates: list[str] | None = None,
        displays: list[Display] | None = None,
    ) -> None:
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors: list[Sensor] = []

    def __str__(self) -> str:
        return (
            f"Car park at {self.location} with a capacity of {self.capacity}"
        )

    def register(self, component: Display | Sensor) -> None:
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            msg = f"argument component was not of type (Display | Sensor), got type: {component}"
            raise TypeError(msg)

    def add_car(self, plate: str) -> None:
        pass

    def remove_car(self, plate: str) -> None:
        pass

    def update_displays(self) -> None:
        pass
