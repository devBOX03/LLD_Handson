from parking_lot.models.vehicle_type import VehicleType
from parking_lot.services.entry_gate_service import EntryGateService

class EntryGateController(object):
    entry_gate_service: EntryGateService = EntryGateService()

    def createTicket(self, vehicle_type: VehicleType):
        return self.entry_gate_service.createTicket(vehicle_type)
