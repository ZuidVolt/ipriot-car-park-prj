from display import Display


class CarPark:
    def __init__(
        self,
        location: str | None,
        capacity: int,
        plates: list[str] | None = None,
        displays: list[Display] | None = None,
    ) -> None:
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self) -> str:
        return (
            f"Car park at {self.location} with a capacity of {self.capacity}"
        )
