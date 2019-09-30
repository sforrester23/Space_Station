# Expeditions should have:
    # Origin (probably gazorpazorp)
    # Desitination
    # spacecraft assigned to it
    # a list of passengers

class Expedition():
    def __init__(self, destination, spacecraft, origin = 'Gazorpazorp'):
        self.origin = origin
        self.destination = destination
        self.spacecraft = spacecraft
        self.passenger_list = []

    def passenger_add(self, ):