from datetime import datetime
from parking_lot.models.vehicle_type import VehicleType

class TicketDTO:
    def __init__(self):
        self._vehicle_type: VehicleType = None
        self._entry_time: datetime = None

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @property
    def entry_time(self):
        return self._entry_time

    @classmethod
    def get_builder(cls):
        return cls.TicketDTOBuilder()

    class TicketDTOBuilder:
        def __init__(self):
            self._ticket_dto: TicketDTO = TicketDTO()

        def set_vehicle_type(self, vehicle_type: VehicleType):
            self._ticket_dto._vehicle_type = vehicle_type
            return self

        def set_entry_time(self, entry_time: datetime):
            self._ticket_dto._entry_time = entry_time
            return self

        def build(self):
            return self._ticket_dto
