import logging
import unittest
from pathlib import Path

from src.car_park import CarPark
from src.display import Display

LOG_PATH = Path("test-display-log")


class TestDisplay(unittest.TestCase):
    def setUp(self) -> None:
        self.display = Display(
            display_id=1,
            message="Welcome to the car park",
            is_on=True,
            logging_level=logging.ERROR,
        )
        self.car_park = CarPark(
            capacity=100,
            location="123 Example Street",
            logging_level=logging.ERROR,
            log_file=LOG_PATH,
        )

    def test_display_initialized_with_all_attributes(self) -> None:
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)

    def test_update(self) -> None:
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

    def test_update_invalid_key(self) -> None:
        with self.assertRaises(ValueError):
            self.display.update({"invalid_key": "This should raise an error"})  # type: ignore[arg-type]

    def test_display_str(self) -> None:
        expected_str = "Display 1: Welcome to the car park"
        self.assertEqual(str(self.display), expected_str)

    def tearDown(self) -> None:
        LOG_PATH.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
