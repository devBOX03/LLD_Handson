class Payment(object):
    def __init__(self):
        self._ticket_id: str = None
        self._amount: int = None
        self._mode: str = None

    @property
    def ticket_id(self) -> int:
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id: int):
        self._ticket_id = ticket_id

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        self._amount = amount

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        self._mode = mode
