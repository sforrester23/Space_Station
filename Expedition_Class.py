# Expeditions should have:
    # Origin (probably gazorpazorp)
    # Desitination
    # spacecraft assigned to it
    # a list of passengers

class Expedition():
    def __init__(self, destination, spacecraft = '', origin = 'Gazorpazorp'):
        self.__origin = origin
        self.__destination = destination
        self.__spacecraft = spacecraft
        self.__passenger_list = []

    def assign_spaceship(self, spaceship):
        self.__spacecraft = spaceship

    def assign_passenger(self, passenger):
        self.__passenger_list.append(passenger)

    def expedition_details(self):
        # We want to send a dictionary with
            # origin, destination, ship, passengers#
        expedition_dictionary = {
            'origin': self.__origin,
            'destination': self.__destination,
            'spacecraft': self.__spacecraft,
            'passenger_list': self.__passenger_list
        }
        return expedition_dictionary

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_ship(self):
        return self.__spacecraft

    def get_passengers(self):
        return self.__passenger_list


    def print_passenger_list(self):
        count = 1
        for passenger in self.get_passengers():
            print('Passenger number {}'.format(count))
            print('Passenger name:', passenger.name)
            print('Passenger Species: ', passenger.species)
            print('Passenger IDR: ', passenger.intergalactic_dna_reg)
            print('///////////////')
            count += 1