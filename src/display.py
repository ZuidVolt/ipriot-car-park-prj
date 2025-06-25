class Display:
    def __init__(
        self, display_id: int, message: str = "", *, is_on: bool = False
    ) -> None:
        self.id = display_id
        self.message = message
        self.is_on = is_on

    def __str__(self) -> str:
        return f"Display {self.id}: {self.message}"

    def update(self) -> None:
        pass
