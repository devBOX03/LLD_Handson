from parking_lot.models.ticket import Ticket
from parking_lot.strategies.fee_strategy import FeeStrategy

class SmallVehicleStrategy(FeeStrategy):
    def calculate_fee(self, ticket: Ticket) -> int:
        # implement calculation
        return 0
