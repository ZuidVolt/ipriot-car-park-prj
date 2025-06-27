import unittest
from pathlib import Path

from src.config import CarParkConfig, Config

LOG_PATH = Path("test-config-log")
CONFIG_PATH = Path("test_config.json")


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config(file_path=CONFIG_PATH)
        self.test_data: CarParkConfig = {
            "location": "123 Example Street",
            "capacity": 100,
            "log_file": str(LOG_PATH),
        }

    def test_write_to_config_file(self) -> None:
        self.config.write(self.test_data)
        self.assertTrue(CONFIG_PATH.exists())

        with CONFIG_PATH.open() as f:
            data = f.read()
            self.assertIn("123 Example Street", data)
            self.assertIn("100", data)
            self.assertIn(str(LOG_PATH), data)

    def test_read_from_config_file(self) -> None:
        self.config.write(self.test_data)
        config_data = self.config.read()
        self.assertEqual(config_data["location"], "123 Example Street")
        self.assertEqual(config_data["capacity"], 100)
        self.assertEqual(config_data["log_file"], str(LOG_PATH))

    def test_read_empty_config_file(self) -> None:
        CONFIG_PATH.write_text("")  # writes over the file to make it empty
        with self.assertRaises(ValueError):
            self.config.read()

    def tearDown(self) -> None:
        CONFIG_PATH.unlink(missing_ok=True)
        LOG_PATH.unlink(missing_ok=True)
