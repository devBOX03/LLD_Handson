from design_pen.v2.models.gel_pen import GelPen
from design_pen.v2.models.pen_body import PenBody
from design_pen.v2.models.pen_ink import PenInk
from design_pen.v2.models.pen_nib import PenNib
from design_pen.v2.models.pencil import Pencil

def test_design_pen():
    pen_body: PenBody = PenBody(length=5.0, diameter=0.5)
    pen_ink: PenInk = PenInk(ink_color="blue")
    pen_nib: PenNib = PenNib(diameter=0.05)
    gel_pen: GelPen = GelPen(pen_body, pen_ink, pen_nib)
    gel_pen.write()
    print(gel_pen.pen_nib)
    gel_pen.pen_nib = "xyz"
    print(gel_pen.pen_nib)
    pencil = Pencil()
    assert gel_pen.pen_ink.ink_color == "blue"
