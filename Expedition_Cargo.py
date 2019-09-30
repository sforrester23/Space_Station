# This class will be used to monitor cargo

from Expedition_Class import *

class Cargo(Expedition):
    def __init__(self, destination, spacecraft, amount, cargo, origin = 'Gazorpazorp'):
        super().__init__(destination, spacecraft, origin)
        self.__origin = origin
        self.__destination = destination
        self.__spacecraft = spacecraft
        self.__passenger_list = []
        self.amount = amount
        self.cargo = cargo

    def pay_tariffs(self):
        return self.amount * 0.8

    def expedition_details(self):
        # We want to send a dictionary with
        # origin, destination, ship, passengers#
        expedition_dictionary = {
            'origin': self.__origin,
            'destination': self.__destination,
            'spacecraft': self.__spacecraft,
            'passenger_list': self.__passenger_list,
            'weight': self.amount,
            'cargo': self.cargo
        }
        return expedition_dictionary

cargo_1= Cargo('tootle', 'bongo', 300, 'cigars')
print(cargo_1.expedition_details())
