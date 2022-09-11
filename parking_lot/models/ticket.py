from datetime import datetime
from parking_lot.models.ticket_status import TicketStatus
from parking_lot.models.vehicle import Vehicle
from parking_lot.models.vehicle_type import VehicleType

class Ticket(object):
    def __init__(self):
        self._ticket_id: int = None
        self._vehicle: Vehicle = None
        self._floor_number: int = None
        self._slot_number: int = None
        self._entry_time: datetime = None
        self._exit_time: datetime = None
        self._status: TicketStatus = None

    @property
    def ticket_id(self) -> int:
        return self._ticket_id

    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle

    @property
    def floor_number(self) -> int:
        return self._floor_number

    @property
    def slot_number(self) -> int:
        return self._slot_number

    @property
    def entry_time(self) -> datetime:
        return self._entry_time

    @property
    def exit_time(self) -> datetime:
        return self._exit_time

    @exit_time.setter
    def exit_time(self, exit_time: datetime):
        self._exit_time = exit_time

    @property
    def status(self) -> TicketStatus:
        return self._status

    @status.setter
    def status(self, status: TicketStatus):
        self._status = status

    @classmethod
    def get_builder(cls):
        return cls.TicketBuilder()

    class TicketBuilder:
        def __init__(self):
            self._ticket: Ticket = Ticket()

        def vehicle(self, vehicle_type: VehicleType):
            vehicle: Vehicle = Vehicle()
            vehicle.type(vehicle_type)
            vehicle.registration_number("NA")
            self._ticket._vehicle = vehicle
            return self

        def entry_time(self):
            self._ticket._entry_time = datetime.now()
            return self

        def floor_number(self, floor_number: int):
            self._ticket._floor_number = floor_number
            return self

        def slot_number(self, slot_number: int):
            self._ticket._slot_number = slot_number
            return self

        def build(self):
            return self._ticket
