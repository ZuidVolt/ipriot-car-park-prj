from pathlib import Path

from .car_park import CarPark
from .config import Config
from .display import Display
from .sensor import EntrySensor, ExitSensor

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# TODO: Write the car park configuration to a file called "moondalup_config.json"
# TODO: Reinitialize the car park object from the "moondalup_config.json" file
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)


def main() -> None:
    car_park = CarPark(
        capacity=100,
        location="Moondalup",
        log_file="moondalup.txt",
        config=Config(file_path="moondalup_config.json"),
    )

    entry_sensor = EntrySensor(sensor_id=1, car_park=car_park, is_active=True)
    exit_sensor = ExitSensor(sensor_id=2, car_park=car_park, is_active=True)
    display = Display(
        display_id=1,
        message="",
        is_on=True,
    )

    car_park.register(display)
    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    for _ in range(10):
        entry_sensor.detect_vehicle()

    for _ in range(2):
        exit_sensor.detect_vehicle()

    car_park.write_config()
    reloaded_car_park = CarPark.from_config(
        config_file=Path("moondalup_config.json")
    )
    print("\nReloaded Car Park Configuration:")
    print(reloaded_car_park)


if __name__ == "__main__":
    main()
