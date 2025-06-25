import logging
from typing import TypedDict

from .utils import strip_dunder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(strip_dunder(__name__))


class DisplayData(TypedDict):
    available_bays: int
    temperature: float


class Display:
    def __init__(
        self, display_id: int, message: str = "", *, is_on: bool = False
    ) -> None:
        self.id = display_id
        self.message = message
        self.is_on = is_on

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"

    def update(self, data: DisplayData) -> None:
        for key, val in data.items():
            display_val = round(val, 1) if isinstance(val, float) else val
            print(f"{key}: {display_val}")


if __name__ == "__main__":
    display = Display(1, "Welcome to the Car Park", is_on=True)
    print(display)
    display.update({
        "available_bays": 10,
        "temperature": 22.55,
    })
