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

        # Set the logging level for this instance
        logger.setLevel(logging_level)

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"

    def update(self, data: DisplayData) -> None:
        if "message" in data and data["message"] is not None:
            self.message = data["message"]
        if "available_bays" in data:
            self.available_bays = data["available_bays"]
        if "temperature" in data:
            self.temperature = data["temperature"]

    def display(self, data: DisplayData) -> None:
        for key, val in data.items():
            display_val = round(val, 1) if isinstance(val, float) else val
            logger.info(f"{key}: {display_val}")

    def update_and_display(self, data: DisplayData) -> None:
        self.update(data)
        self.display(data)


if __name__ == "__main__":
    display = Display(1, "Welcome to the Car Park", is_on=True)
    print(display)
    display.update_and_display({
        "message": "Car Park Full",
        "available_bays": 10,
        "temperature": 22.55,
    })
