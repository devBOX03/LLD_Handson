from design_pen.v2.interfaces.writable_interface import Writable

class Pencil(Writable):
    def write(self):
        print("Pencil writing")