from abc import ABC, abstractmethod

from car_park import CarPark


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

    @abstractmethod
    def update_car_park(self, plate: str) -> None:
        pass

    @abstractmethod
    def detect_car(self) -> None:
        pass


class EntrySensor(Sensor):
    def update_car_park(self, plate: str) -> None:
        pass


class ExitSensor(Sensor):
    def update_car_park(self, plate: str) -> None:
        pass
