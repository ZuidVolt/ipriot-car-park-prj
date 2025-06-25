class Sensor:
    def __init__(self, senor_id: int, car_park, *, is_active: bool) -> None:
        self.senor_id = senor_id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self) -> str:
        status: str = ""
        status = "is active" if self.is_active else "is not active"
        return f"Display {self.senor_id}, Status: the senor {status}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
