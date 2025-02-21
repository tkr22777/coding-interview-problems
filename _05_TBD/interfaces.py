from abc import ABC, abstractmethod


class AnimalInterface(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


# Implementing the interface
class Dog(AnimalInterface):
    def make_sound(self):
        return "Bark"

    def move(self):
        return "Runs"

