import logging

from utils import strip_dunder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(strip_dunder(__name__))


class Display:
    def __init__(
        self, display_id: int, message: str = "", *, is_on: bool = False
    ) -> None:
        self.id = display_id
        self.message = message
        self.is_on = is_on

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"

    def update(self, data: dict[str, str | int]) -> None:
        for key, value in data.items():
            print(f"{key}: {value}")
