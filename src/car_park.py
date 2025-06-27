import logging
import random
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from .config import CarParkConfig, Config
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
    def __init__(
        self,
        capacity: int,
        plates: list[str] | None = None,
        displays: list[Display] | None = None,
        location: str = "Unknown Location",
        *,
        log_file: str | Path = Path("log.txt"),
        config: Config | None = None,
        logging_level: int = logging.INFO,
    ) -> None:
        self.location = str(location)
        self.capacity = int(capacity)
        self.plates = plates or []
        self.displays = displays or []
        self.sensors: list[Sensor] = []
        self.log_file: Path = (
            log_file if isinstance(log_file, Path) else Path(log_file)
        )
        self.log_file.touch(exist_ok=True)
        self.config = config or Config()

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
        """Calculate the number of available bays in the car park."""
        available_bays: int = max(0, self.capacity - len(self.plates))
        if self.capacity - len(self.plates) < 0:
            logger.warning(
                "The number of cars exceeds the capacity of the car park."
            )
        return available_bays

    def register(self, component: Display | Sensor) -> None:
        """Register a Display or Sensor component to the car park."""
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):  # type: ignore[unreachable]
            self.displays.append(component)
        else:
            msg = f"argument component was not of type (Display | Sensor), got type: {component}"
            raise TypeError(msg)

    def add_car(self, plate: str) -> None:
        """Add a car to the car park by its plate number."""
        self.plates.append(plate)
        self.update_displays(event_type="entered")
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate: str) -> None:
        """Remove a car from the car park by its plate number."""
        try:
            self.plates.remove(plate)
        except ValueError:
            logger.warning(
                f"Car with plate {plate} not found in the car park."
            )
        self.update_displays(event_type="exited")
        self._log_car_activity(plate, "exited")

    @staticmethod
    def _get_rand_temp() -> float:
        return round(random.uniform(15.0, 30.0), 1)

    def update_displays(
        self,
        event_type: str,
    ) -> None:
        """Update the displays with the current state of the car park.
        event_type: str, can be "entered", "exited", or any other string
        """
        display_message: str

        match event_type:
            case _ if self.available_bays == 0:
                display_message = "Car Park Full!"
            case "exited":
                display_message = (
                    f"Thank you for staying at {self.location} Car Park"
                )
            case "entered":
                display_message = f"Welcome to {self.location} Car Park"
            case _:
                display_message = f"Welcome to {self.location} Car Park"  # could be a custom message instead

        data: DisplayData = {
            "available_bays": self.available_bays,
            "temperature": self._get_rand_temp(),
            "message": display_message,
        }
        for display in self.displays:
            display.update_and_display(data, is_display_on=True)

    def write_config(self) -> None:
        """Write the current configuration of the car park to a config file."""
        config_data: CarParkConfig = {
            "location": self.location,
            "capacity": self.capacity,
            "log_file": str(self.log_file),
        }
        self.config.write(config_data)

    @classmethod
    def from_config(cls, config_file: Path = Path("config.json")) -> "CarPark":
        """Create a CarPark instance from a configuration file."""
        # not completely happy with this as i would like somehow pass the self.config attribute
        # instead of creating a new instance of Config
        config: Config = Config(file_path=config_file)
        try:
            config_data: CarParkConfig = config.read()
        except ValueError:
            logger.error("Failed to read configuration")
            raise

        return cls(
            capacity=config_data["capacity"],
            location=config_data["location"],
            log_file=config_data["log_file"],
            config=config,
        )


if __name__ == "__main__":
    pass
