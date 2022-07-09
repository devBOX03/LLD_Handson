import abc

from parking_lot.models.ticket import Ticket

class FeeStrategy(abc.ABCMeta):
    @abc.abstractmethod
    def calculate_fee(self, ticket: Ticket) -> int:
        pass
