from __future__ import annotations

import logging
import random
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # this is to avoid circular import while still allowing static type checking
    from car_park import CarPark

from .utils import strip_dunder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(strip_dunder(__name__))


class Sensor(ABC):
    def __init__(
        self, senor_id: int, car_park: CarPark, *, is_active: bool
    ) -> None:
        self.senor_id = senor_id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self) -> str:
        status: str = ""
        status = "is active" if self.is_active else "is not active"
        return f"Display {self.senor_id}, Status: the senor {status}"

    def _scan_plate(self) -> str:
        return "FAKE-" + format(random.randint(0, 999), "03d")

    @abstractmethod
    def update_car_park(self, plate: str) -> None:
        pass

    def detect_vehicle(self) -> None:
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate: str) -> None:
        self.car_park.add_car(plate)
        logger.info(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def _scan_plate(self) -> str:
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate: str) -> None:
        self.car_park.remove_car(plate)
        logger.info(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
