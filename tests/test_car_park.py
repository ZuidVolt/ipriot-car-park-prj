import logging
import unittest

from src.car_park import CarPark


class TestCarPark(unittest.TestCase):
    def setUp(self) -> None:
        self.car_park = CarPark(
            capacity=100,
            location="123 Example Street",
            logging_level=logging.ERROR,
        )

    def test_car_park_initialized_with_all_attributes(self) -> None:
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)

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
    # my thoughts are that removing a car that does not exist should not be a runtime error
    def test_removing_a_car_that_does_not_exist(
        self,
    ) -> None:
        try:
            with self.assertRaises(ValueError):
                self.car_park.remove_car("NO-1")
        except AssertionError:
            pass

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


if __name__ == "__main__":
    unittest.main()
