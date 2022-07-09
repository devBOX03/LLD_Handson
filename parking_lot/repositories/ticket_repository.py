from typing import List
from parking_lot.models.ticket import Ticket

class TicketRepository:
    tickets: List[Ticket] = []
    def save(self, ticket: Ticket) -> None:
        self.tickets.append(ticket)
        return ticket
