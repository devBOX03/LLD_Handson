from parking_lot.controllers.entry_gate_controller import EntryGateController
from parking_lot.models.ticket import Ticket
from parking_lot.models.vehicle_type import VehicleType

def test_entry_gate_controller():
    entry_gate_controller: EntryGateController = EntryGateController()
    ticket: Ticket = entry_gate_controller.createTicket(VehicleType.SMALL)
    assert isinstance(ticket, Ticket)
    assert ticket.vehicle.type == VehicleType.SMALL