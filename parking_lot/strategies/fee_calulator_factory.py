from parking_lot.models.vehicle_type import VehicleType
from parking_lot.strategies.large_vehicle_strategy import LargeVehicleStrategy
from parking_lot.strategies.medium_vehicle_strategy import MediumVehicleStrategy
from parking_lot.strategies.small_vehicle_strategy import SmallVehicleStrategy


class FeeCalculatorFactory:
    @classmethod
    def get_strategy(cls, vehicle_type: VehicleType):
        if vehicle_type == VehicleType.LARGE:
            return LargeVehicleStrategy()
        elif vehicle_type == VehicleType.MEDIUM:
            return MediumVehicleStrategy()
        elif vehicle_type == VehicleType.SMALL:
            return SmallVehicleStrategy()
        raise Exception("Invalid vehicle type")
