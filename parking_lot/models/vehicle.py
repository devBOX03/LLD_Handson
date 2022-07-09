from parking_lot.models.vehicle_type import VehicleType

class Vehicle(object):
    def __init__(self):
        self._registration_number: str = None
        self._type: VehicleType = None

    @property
    def registration_number(self) -> str:
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number: str):
        self._registration_number = registration_number

    @property
    def type(self) -> VehicleType:
        return self._type

    @type.setter
    def type(self, type: VehicleType):
        self._type = type
