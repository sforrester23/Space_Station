# Spaceships should have
    # Captain
    # name
    # intergalactic_warp_drive_signature

class Spaceship():
    def __init__(self, captain, name, intergalactic_warp_drive_signature):
        self.captain = captain
        self.__name = name
        self.__intergalactic_warp_drive_signature = intergalactic_warp_drive_signature

    def identify_ship(self):
        return self.__intergalactic_warp_drive_signature

    def identify_name(self):
        return self.__name

    def change_name(self, new_name):
        self.__name = new_name


