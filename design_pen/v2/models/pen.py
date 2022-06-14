from abc import ABC, abstractmethod

from design_pen.v2.interfaces.writable_interface import Writable
from design_pen.v2.models.pen_body import PenBody
from design_pen.v2.models.pen_ink import PenInk
from design_pen.v2.models.pen_nib import PenNib

class Pen(ABC, Writable):
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
    def refill(self) -> None:
        pass