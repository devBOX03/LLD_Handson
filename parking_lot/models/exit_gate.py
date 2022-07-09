from parking_lot.models.operator import Operator
from parking_lot.models.gate import Gate

class ExitGate(Gate):
    def __init__(self):
        self._opeator: Operator
        self._location: str

    @property
    def opeator(self) -> Operator:
        return self._opeator

    @opeator.setter
    def opeator(self, opeator: Operator):
        self._opeator = opeator

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, location: str):
        self._location = location

    def payment_counter(self):
        ...
