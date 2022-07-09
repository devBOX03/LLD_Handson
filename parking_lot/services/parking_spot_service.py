from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.repositories.parking_spot_repository import ParkingSpotRepository

class ParkingSpotService:
    parking_spot_repo: ParkingSpotRepository = ParkingSpotRepository()

    def mark_slot_booked(self, spot: ParkingSpot) -> None:
        self.parking_spot_repo.save(spot)

    def get_parking_spot(self, spot_id: int):
        return self.parking_spot_repo.find_by_id(spot_id)
