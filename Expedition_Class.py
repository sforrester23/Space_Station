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

    def passenger_add(self, passenger):
        self.__passenger_list.append(passenger)

    def expedition_details(self, origin, destination, spacecraft, passenger_list):
        # We want to send a dictionary with
            # origin, destination, ship, passengers#
        expedition_dictionary = {
            'origin': self.__origin,
            'destination': self.__destination,
            'spacecraft': self.__spacecraft,
            'passenger list': self.__passenger_list
        }
        return expedition_dictionary