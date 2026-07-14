from dataclasses import dataclass


@dataclass
class Disk:

    index: int

    model: str

    size: int

    interface: str

    serial: str

    manufacturer: str

    partitions: int

    deviceid: str

    sectors: int

    @property
    def size_gb(self):
        return self.size / (1024 ** 3)