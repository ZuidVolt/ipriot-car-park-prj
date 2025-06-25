import logging
import unittest

from src.car_park import CarPark
from src.sensor import EntrySensor, ExitSensor, Sensor


class TestSensor(unittest.TestCase):
    def setUp(self) -> None:
        self.car_park = CarPark(
            capacity=100,
            location="123 Example Street",
            logging_level=logging.ERROR,
        )
        self.entry_sensor = EntrySensor(
            sensor_id=1,
            car_park=self.car_park,
            is_active=True,
            logging_level=logging.ERROR,
        )
        self.exit_sensor = ExitSensor(
            sensor_id=2,
            car_park=self.car_park,
            is_active=True,
            logging_level=logging.ERROR,
        )

    def test_sensor_initialization(self) -> None:
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertTrue(self.entry_sensor.is_active)
        self.assertTrue(self.exit_sensor.is_active)

    def test_detect_vehicle(self) -> None:
        # EntrySensor should add a car to the car park
        initial_count = len(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count + 1)

        # ExitSensor should remove a car from the car park
        # First, ensure there is at least one car to remove
        self.entry_sensor.detect_vehicle()
        plates_before_exit = self.car_park.plates.copy()
        self.exit_sensor.detect_vehicle()
        # After exit, the number of plates should decrease by 1
        self.assertEqual(
            len(self.car_park.plates), len(plates_before_exit) - 1
        )

    def test_update_car_park(self) -> None:
        # Test EntrySensor's update_car_park
        plate = "TEST-001"
        self.entry_sensor.update_car_park(plate)
        self.assertIn(plate, self.car_park.plates)

        # Test ExitSensor's update_car_park
        self.exit_sensor.update_car_park(plate)
        self.assertNotIn(plate, self.car_park.plates)


if __name__ == "__main__":
    unittest.main()
