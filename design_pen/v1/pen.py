from abc import ABC, abstractmethod
from design_pen.v1.pen_body import PenBody
from design_pen.v1.pen_ink import PenInk
from design_pen.v1.pen_nib import PenNib

class Pen(ABC):
    @property
    @abstractmethod
    def pen_body(self) -> PenBody:
        ...
    @property
    @abstractmethod
    def pen_ink(self) -> PenInk:
        ...
    @property
    @abstractmethod
    def pen_nib(self) -> PenNib:
        ...

    @abstractmethod
    def write(self) -> None:
        pass
    @abstractmethod
    def refill(self) -> None:
        pass