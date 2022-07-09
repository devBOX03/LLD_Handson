from typing import List
from parking_lot.models.parking_spot import ParkingSpot

class ParkingFloor(object):
    def __init__(self):
        self._number: int = None
        self._name: str = None
        self._parking_spots: List[ParkingSpot] = []

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    def number(self, floor_number: int) -> None:
        self._number = floor_number

    @property
    def name(self) -> int:
        return self._name

    @name.setter
    def name(self, floor_name: int) -> None:
        self._name = floor_name

    @property
    def parking_spots(self) -> int:
        return self._parking_spots

    @parking_spots.setter
    def parking_spots(self, floor_parking_spots: int) -> None:
        self._parking_spots = floor_parking_spots
