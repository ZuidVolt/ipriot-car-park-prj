import json
from pathlib import Path
from typing import TypedDict


class CarParkConfig(TypedDict):
    location: str
    capacity: int
    log_file: str


class Config:
    def __init__(self, file_path: str | Path = "config.json") -> None:
        self.file_path: Path = (
            file_path if isinstance(file_path, Path) else Path(file_path)
        )

    def write(self, config_data: CarParkConfig) -> None:
        with self.file_path.open("w") as f:
            json.dump(
                {
                    "location": config_data["location"],
                    "capacity": config_data["capacity"],
                    "log_file": str(config_data["log_file"]),
                },
                f,
            )

    def read(self) -> CarParkConfig:
        with self.file_path.open() as f:
            config = json.load(f)
        if not config:
            msg = "Configuration file is empty or invalid."
            raise ValueError(msg)
        return CarParkConfig(
            location=config["location"],
            capacity=config["capacity"],
            log_file=(config["log_file"]),
        )
