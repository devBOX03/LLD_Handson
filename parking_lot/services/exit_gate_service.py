
from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.parking_spot_status import ParkingSpotStatus
from parking_lot.models.ticket import Ticket
from parking_lot.services.fee_calculator_service import FeeCalculatorService
from parking_lot.services.parking_spot_service import ParkingSpotService
from parking_lot.services.ticket_service import TicketService
class ExitGateService:
    # fee calculator service
    fee_calculator_service: FeeCalculatorService = FeeCalculatorService()
    # parking spot service
    parking_spot_service: ParkingSpotService = ParkingSpotService()
    # ticket service
    ticket_service: TicketService = TicketService()

    def close_ticket(self, ticket: Ticket, payment_recieved: int):
        # calulate total fee
        total_fee: int = FeeCalculatorService.calculate_fee(ticket)
        # compare both fee and close ticket if payment done else raise exception
        if payment_recieved < total_fee:
            raise Exception(f"Pending amount: {total_fee - payment_recieved}")
        self.clear_parking_spot(ticket)
        self.ticket_service.close_ticket(ticket)

    def clear_parking_spot(self, ticket: Ticket):
        # clear parking spot
        parking_spot: ParkingSpot = self.parking_spot_service.get_parking_spot(ticket.slot_number)
        parking_spot.status = ParkingSpotStatus.AVAILABLE
