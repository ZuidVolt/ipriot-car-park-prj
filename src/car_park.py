from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .sensor import Sensor
from .utils import strip_dunder

if TYPE_CHECKING:  # this is to avoid circular import while still allowing static type checking
    from display import Display, DisplayData  # noqa: TC004
    from sensor import Sensor  # noqa: TC004

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(strip_dunder(__name__))


class CarPark:
    def __init__(
        self,
        capacity: int,
        plates: list[str] | None = None,
        displays: list[Display] | None = None,
        location: str = "Unknown Location",
        logging_level: int = logging.INFO,
    ) -> None:
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors: list[Sensor] = []

        # Set the logging level for this instance
        logger.setLevel(logging_level)

        if self.capacity < 0:
            msg = "Capacity must be a positive integer."
            raise ValueError(msg)
        if not self.location:
            logger.debug(
                "Location is an empty string (or possible the wrong type)."
            )
            self.location = "Unknown Location"

    def __str__(self) -> str:
        return (
            f"Car park at {self.location} with a capacity of {self.capacity}"
        )

    @property
    def available_bays(self) -> int:
        available_bays: int = max(0, self.capacity - len(self.plates))
        if self.capacity - len(self.plates) < 0:
            logger.warning(
                "The number of cars exceeds the capacity of the car park."
            )
        return available_bays

    def register(self, component: Display | Sensor) -> None:
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):  # type: ignore[unreachable]
            self.displays.append(component)
        else:
            msg = f"argument component was not of type (Display | Sensor), got type: {component}"
            raise TypeError(msg)

    def add_car(self, plate: str) -> None:
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate: str) -> None:
        try:
            self.plates.remove(plate)
        except ValueError:
            logger.warning(
                f"Car with plate {plate} not found in the car park."
            )
        self.update_displays()

    def update_displays(self) -> None:
        data: DisplayData = {
            "available_bays": self.available_bays,
            "temperature": 25,
        }
        for display in self.displays:
            display.update(data)


if __name__ == "__main__":
    pass
