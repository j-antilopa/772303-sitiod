from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator


class AbstractFactory(ABC):

    @abstractmethod
    def create_product(self, data):
        pass

class TrainFactory(AbstractFactory):
    def create_product(self, data):
        return Train(*data)

class BusFactory(AbstractFactory):
    def create_product(self, data):
        return Bus(*data)


class Vehicle(Iterator):
    _position: int = 0

    def __init__(self, number, time_start, time_end, station_start, station_end, ticket_price, platform):
        self.number, self.time_start, self.time_end, self.station_start, self.station_end, self.ticket_price, self.platform = number, time_start, time_end, station_start, station_end, ticket_price, platform

    def __next__(self):
        fields = list(self.__dict__.keys())
        try:
            if self._position == len(fields)-1:
                raise StopIteration()
            value = fields[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return self.__dict__[value]

class Train(Vehicle):
    def __init__(self, number, time_start, time_end, station_start, station_end, ticket_price, platform, type):
        Vehicle.__init__(self, number, time_start, time_end, station_start, station_end, ticket_price, platform)
        self.type = type



class Bus(Vehicle):
    def __init__(self, number, time_start, time_end, station_start, station_end, ticket_price, platform, bus_brand):
        Vehicle.__init__(self, number, time_start, time_end, station_start, station_end, ticket_price, platform)
        self.bus_brand = bus_brand
