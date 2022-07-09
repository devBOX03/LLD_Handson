from parking_lot.models.parking_spot_status import ParkingSpotStatus
from parking_lot.models.vehicle_type import VehicleType

class ParkingSpot(object):
    def __init__(self):
        self._spot_id: int = None
        self._floor_number: int = None
        self._status: ParkingSpotStatus = None
        self._vehicle_type: VehicleType = None

    @property
    def spot_id(self) -> int:
        return self._spot_id

    @spot_id.setter
    def spot_id(self, spot_id: int):
        self._spot_id = spot_id

    @property
    def floor_number(self) -> int:
        return self._floor_number

    @floor_number.setter
    def floor_number(self, floor_number: int):
        self._floor_number = floor_number

    @property
    def status(self) -> ParkingSpotStatus:
        return self._status

    @status.setter
    def status(self, status: ParkingSpotStatus):
        self._status = status

    @property
    def vehicle_type(self) -> VehicleType:
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type: VehicleType):
        self._vehicle_type = vehicle_type
