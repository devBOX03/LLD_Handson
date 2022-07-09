import abc
from parking_lot.models.operator import Operator

class Gate(abc.ABC):

    @property
    @abc.abstractclassmethod
    def opeator(self) -> Operator:
        ...

    # @opeator.setter
    # def opeator(self, opeator: Operator):
    #     self._opeator = opeator

    @property
    @abc.abstractclassmethod
    def location(self) -> str:
        ...

    # @location.setter
    # def location(self, location: str):
    #     self._location = location