from design_pen.v1.gel_pen import GelPen
from design_pen.v1.pen_body import PenBody
from design_pen.v1.pen_ink import PenInk
from design_pen.v1.pen_nib import PenNib

def test_design_pen():
    pen_body: PenBody = PenBody(length=5.0, diameter=0.5)
    pen_ink: PenInk = PenInk(ink_color="blue")
    pen_nib: PenNib = PenNib(diameter=0.05)
    gel_pen: GelPen = GelPen(pen_body, pen_ink, pen_nib)
    gel_pen.write()
    assert gel_pen.pen_nib.diameter == 0.05