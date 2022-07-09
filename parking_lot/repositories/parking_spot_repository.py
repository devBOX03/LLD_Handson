from typing import List
from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.vehicle_type import VehicleType
from parking_lot.models.parking_spot_status import ParkingSpotStatus

class ParkingSpotRepository:
    parking_spots: List[ParkingSpot] = []

    def save(self, parking_spot: ParkingSpot):
        self.parking_spots.append(parking_spot)

    def find_available_parking_spot_by_vehcle_type(self, vehicle_type: VehicleType):
        for spot in self.parking_spots:
            if spot.vehicle_type == vehicle_type and spot.status == ParkingSpotStatus.AVAILABLE:
                return spot
        return None

    def find_by_id(self, spot_id: int):
        for spot in self.parking_spots:
            if spot.spot_id == spot_id:
                return spot
        return None
