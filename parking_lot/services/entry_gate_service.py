from parking_lot.dtos.ticket_dto import TicketDTO
from parking_lot.models.ticket import Ticket
from parking_lot.models.vehicle_type import VehicleType
from parking_lot.models.parking_spot_status import ParkingSpotStatus
from parking_lot.services.parking_spot_service import ParkingSpotService
from parking_lot.services.slot_allocation_service import SlotAllocationService
from parking_lot.services.ticket_service import TicketService

class EntryGateService:
    # spot allocation service
    slot_allocation_service: SlotAllocationService = SlotAllocationService()
    # parking spot service
    parking_spot_service: ParkingSpotService = ParkingSpotService()
    # ticket creation service
    ticket_service: TicketService = TicketService()

    def createTicket(self, vehicle_type: VehicleType):
        # check ticket availbily and get parking spot
        parking_spot = self.slot_allocation_service.allocate_slot(vehicle_type)
        if parking_spot is None:
            return None
        # book parking spot
        parking_spot.status = ParkingSpotStatus.FILLED
        self.parking_spot_service.mark_slot_booked(parking_spot)
        # create ticket
        ticket: Ticket = self.ticket_service.create_ticket(vehicle_type, parking_spot)
        # send ticket DTO
        return TicketDTO \
                .get_builder() \
                .set_entry_time(ticket.entry_time) \
                .set_vehicle_type(ticket.vehicle.type) \
                .build()
