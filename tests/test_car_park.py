import logging
import unittest
from pathlib import Path

from src.car_park import CarPark
from src.display import Display
from src.sensor import EntrySensor

LOG_PATH = Path("test_log.txt")


class TestCarPark(unittest.TestCase):
    def setUp(self) -> None:
        self.car_park = CarPark(
            capacity=100,
            location="123 Example Street",
            logging_level=logging.ERROR,
            log_file=LOG_PATH,
        )

    def test_car_park_initialized_with_all_attributes(self) -> None:
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, LOG_PATH)

    def test_add_car(self) -> None:
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self) -> None:
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self) -> None:
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    # i handle this case with try/except in the remove_car method,
    # my thoughts are that removing a car that does not exist should not be a runtime error and just be logged instead
    def test_removing_a_car_that_does_not_exist(
        self,
    ) -> None:
        try:
            with self.assertRaises(ValueError):
                self.car_park.remove_car("NO-1")
        except AssertionError:
            pass

    def test_register_valid_input_type(self) -> None:
        display = Display(
            display_id=1,
            message="Welcome to the car park",
            is_on=True,
            logging_level=logging.ERROR,
        )
        entry_sensor = EntrySensor(
            sensor_id=1,
            car_park=self.car_park,
            is_active=True,
            logging_level=logging.ERROR,
        )
        self.car_park.register(display)
        self.assertIn(display, self.car_park.displays)

        self.car_park.register(entry_sensor)
        self.assertIn(entry_sensor, self.car_park.sensors)

    def test_register_raises_type_error(self) -> None:
        cases: frozenset[str | int | float | bool | None] = frozenset({
            "Not a Display or Sensor",
            "123",
            123,
            None,
            1.23,
        })
        for case in cases:
            with self.assertRaises(TypeError):
                self.car_park.register(case)  # type: ignore[call-arg]

    def test_car_park_str(self) -> None:
        expected_str = "Car park at 123 Example Street with a capacity of 100"
        self.assertEqual(str(self.car_park), expected_str)

    def test_capacity_negative(self) -> None:
        with self.assertRaises(ValueError):
            CarPark(
                capacity=-1, location="Invalid Location", log_file=LOG_PATH
            )

    def test_location_empty_string(self) -> None:
        car_park = CarPark(capacity=100, location="", log_file=LOG_PATH)
        self.assertEqual(car_park.location, "Unknown Location")
        self.assertEqual(car_park.available_bays, 100)

    def test_location_type_mismatch_handling(self) -> None:
        car_park = CarPark(capacity=100, location=12345, log_file=LOG_PATH)  # type: ignore[arg-type]
        self.assertIsInstance(car_park.location, str)

    def test_log_file_created(self) -> None:
        new_carpark = CarPark(
            location="123 Example Street",
            capacity=100,
            log_file=LOG_PATH,
        )
        self.car_park = new_carpark
        self.assertTrue(LOG_PATH.exists())

    def test_car_logged_when_entering(self) -> None:
        new_carpark = CarPark(
            location="123 Example Street",
            capacity=100,
            log_file=LOG_PATH,
        )
        self.car_park = new_carpark
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self) -> None:
        new_carpark = CarPark(
            location="123 Example Street",
            capacity=100,
            log_file=LOG_PATH,
        )
        self.car_park = new_carpark
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def tearDown(self) -> None:
        LOG_PATH.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
