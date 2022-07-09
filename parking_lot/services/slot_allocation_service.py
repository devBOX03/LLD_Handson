

from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.vehicle_type import VehicleType
from parking_lot.repositories.parking_spot_repository import ParkingSpotRepository


class SlotAllocationService:
    parking_spot_repo: ParkingSpotRepository = ParkingSpotRepository()

    def allocate_slot(self, vehicle_type: VehicleType) -> ParkingSpot:
        return self.parking_spot_repo.find_available_parking_spot_by_vehcle_type(vehicle_type)
