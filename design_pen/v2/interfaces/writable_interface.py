import abc
class Writable(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def write(self) -> None:
        pass
