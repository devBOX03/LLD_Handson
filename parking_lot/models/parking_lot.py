from typing import List
from parking_lot.models.entry_gate import EntryGate
from parking_lot.models.exit_gate import ExitGate
from parking_lot.models.parking_floor import ParkingFloor

class ParkingLot(object):
    def __init__(self):
        self._address: str = None
        self._floors: List[ParkingFloor] = []
        self._entry_gates: List[EntryGate] = []
        self._exit_gates: List[ExitGate] = []

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @property
    def floors(self) -> List[ParkingFloor]:
        return self._floors

    @floors.setter
    def floors(self, floors: List[ParkingFloor]):
        self._floors = floors

    @property
    def entry_gates(self) -> List[EntryGate]:
        return self._entry_gates

    @entry_gates.setter
    def entry_gates(self, entry_gates: List[EntryGate]):
        self._entry_gates = entry_gates

    @property
    def exit_gates(self) -> List[ExitGate]:
        return self._exit_gates

    @exit_gates.setter
    def exit_gates(self, exit_gates: List[ExitGate]):
        self._exit_gates = exit_gates
