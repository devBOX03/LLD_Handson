from parking_lot.models.ticket import Ticket
from parking_lot.strategies.fee_calulator_factory import FeeCalculatorFactory
from parking_lot.strategies.fee_strategy import FeeStrategy

class FeeCalculatorService:
    def calculate_fee(self, ticket: Ticket) -> int:
        fee_strategy: FeeStrategy = FeeCalculatorFactory.get_strategy(ticket.vehicle.type)
        return fee_strategy.calculate_fee(ticket)
