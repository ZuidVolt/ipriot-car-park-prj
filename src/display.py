import logging
from typing import TypedDict

from .utils import strip_dunder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(strip_dunder(__name__))


class DisplayData(TypedDict, total=False):
    message: str | None
    available_bays: int
    temperature: float


class Display:
    def __init__(
        self,
        display_id: int,
        message: str = "",
        logging_level: int = logging.INFO,
        *,
        is_on: bool = False,
    ) -> None:
        self.id = display_id
        self.message = message
        self.is_on = is_on
        self.available_bays: int = 0
        self.temperature: float = 0.0

        # Set the logging level for this instance
        logger.setLevel(logging_level)

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"

    def update(self, data: DisplayData) -> None:
        """Update the display with new data."""
        if "message" in data and data["message"] is not None:
            self.message = data["message"]
        if "available_bays" in data:
            self.available_bays = data["available_bays"]
        if "temperature" in data:
            self.temperature = data["temperature"]
        if (
            "message" not in data
            and "available_bays" not in data
            and "temperature" not in data
        ):
            msg = "Data must contain at least one of 'message', 'available_bays', or 'temperature' fields."
            raise ValueError(msg)

    def display(self, *, is_on: bool | None = None) -> None:
        """Display the current data on the display."""
        display_is_on = is_on if is_on is not None else self.is_on

        if not display_is_on:
            logger.info(f"Display {self.id} is off. No data to show.")
            return

        data_to_display: DisplayData = {
            "message": self.message,
            "available_bays": self.available_bays,
            "temperature": self.temperature,
        }
        logger.info(f"--- Display {self.id} Output ---")
        for key, val in data_to_display.items():
            display_val = round(val, 1) if isinstance(val, float) else val
            logger.info(f"  {key}: {display_val}")
        logger.info("----------------------------")

    def update_and_display(
        self, data: DisplayData, *, is_display_on: bool | None = None
    ) -> None:
        """Update the display with new data and then display it."""
        self.update(data)
        self.display(is_on=is_display_on)


if __name__ == "__main__":
    display = Display(1, "Welcome to the Car Park", is_on=True)
    print(display)
    display.update_and_display(
        {
            "message": "Car Park Full",
            "available_bays": 10,
            "temperature": 22.55,
        },
        is_display_on=True,
    )
