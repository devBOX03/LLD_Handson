from design_pen.v1.pen import Pen
from design_pen.v1.pen_body import PenBody
from design_pen.v1.pen_ink import PenInk
from design_pen.v1.pen_nib import PenNib

class GelPen(Pen):
    def __init__(self, pen_body: PenBody, pen_ink: PenInk, pen_nib: PenNib):
        self._pen_body = pen_body
        self._pen_ink = pen_ink
        self._pen_nib = pen_nib

    @property
    def pen_body(self) -> PenBody:
        return self._pen_body
    
    @pen_body.setter
    def pen_body(self, pen_body: PenBody) -> None:
        self._pen_body = pen_body
    
    @property
    def pen_ink(self) -> PenBody:
        return self._pen_ink
    
    @pen_ink.setter
    def pen_ink(self, pen_ink: PenBody) -> None:
        self._pen_ink = pen_ink
    
    @property
    def pen_nib(self) -> PenBody:
        return self._pen_nib
    
    @pen_nib.setter
    def pen_nib(self, pen_nib: PenBody) -> None:
        self._pen_nib = pen_nib

    def write(self) -> None:
        print("Writing")

    def refill(self) -> None:
        print("refilling")
