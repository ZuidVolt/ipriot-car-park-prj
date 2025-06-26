import logging
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from .display import Display
from .sensor import Sensor
from .utils import strip_dunder

if TYPE_CHECKING:
    from display import DisplayData

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(strip_dunder(__name__))


class CarPark:
    def __init__(  # noqa: PLR0917
        self,
        capacity: int,
        plates: list[str] | None = None,
        displays: list[Display] | None = None,
        location: str = "Unknown Location",
        log_file: str | Path = Path("log.txt"),
        logging_level: int = logging.INFO,
    ) -> None:
        self.location = str(location)
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors: list[Sensor] = []
        self.log_file: Path = (
            log_file if isinstance(log_file, Path) else Path(log_file)
        )
        self.log_file.touch(exist_ok=True)

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

    def _log_car_activity(self, plate: str, action: str) -> None:
        with self.log_file.open("a") as f:
            f.write(
                f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n"  # noqa: DTZ005
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
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate: str) -> None:
        try:
            self.plates.remove(plate)
        except ValueError:
            logger.warning(
                f"Car with plate {plate} not found in the car park."
            )
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self) -> None:
        data: DisplayData = {
            "available_bays": self.available_bays,
            "temperature": 25,
        }
        for display in self.displays:
            display.update(data)


if __name__ == "__main__":
    pass
