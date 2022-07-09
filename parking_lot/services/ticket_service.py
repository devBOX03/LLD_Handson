from datetime import datetime
from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.ticket import Ticket
from parking_lot.models.ticket_status import TicketStatus
from parking_lot.models.vehicle_type import VehicleType
from parking_lot.repositories.ticket_repository import TicketRepository

class TicketService:
    ticket_repo: TicketRepository = TicketRepository()

    def create_ticket(self, vehicle_type: VehicleType, spot: ParkingSpot) -> Ticket:
        ticket: Ticket = Ticket \
                         .get_builder() \
                         .vehicle(vehicle_type) \
                         .floor_number(spot.floor_number) \
                         .slot_number(spot.spot_id) \
                         .entry_time() \
                         .build()
        return self.ticket_repo.save(ticket)

    def close_ticket(self, ticket: Ticket):
        ticket.exit_time = datetime.now()
        ticket.status = TicketStatus.DONE
