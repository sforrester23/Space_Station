# import all classes needed here
from Passenger_Class import *
from Spaceship_Class import *
from Expedition_Class import *

# create objects here

    # create 6 passengers
passenger_1=Passenger('Mr Poopy Butthole', '???', '001')
passenger_2=Passenger('Birdperson', 'Birdperson', '008')
passenger_3=Passenger('Jerry Smith', 'Human', '004')
passenger_4=Passenger('One Million Ants', 'Ant Person', '005')
passenger_5=Passenger('Reverse Giraffe', 'Parasite', '003')
passenger_6=Passenger('Squanch', 'Squanch', '002')
    # generate 3 spaceships +1
ship_1 = Spaceship('Morgan', 'RPS', 'XYZ1015')
ship_2 = Spaceship('Marvel', 'Disappointos', 'GPO6185')
ship_3 = Spaceship('Crunch', 'The Milano', 'TUV8845')
ship_4 = Spaceship('Cage', 'Nicolaus Excelsior', 'CAGE1776')
    # generate 3 expeditions
expedition_1 = Expedition('Mars', ship_1)
expedition_2 = Expedition('Alpha Centuri A', ship_2)
expedition_3 = Expedition('Titan', ship_3)

        # keep list of generated expeditions
expedition_list = [expedition_1, expedition_2, expedition_3]
        # assign a spacecraft to each one
expedition_3.assign_spaceship(ship_4)
            # (should be able to assign on creation of object OR post_facto)
    # assign to each expedition, two passengers (append, method)
expedition_1.assign_passenger(passenger_1)
expedition_1.assign_passenger(passenger_2)
# print(expedition_1.expedition_details())

expedition_2.assign_passenger(passenger_3)
expedition_2.assign_passenger(passenger_4)
# print(expedition_2.expedition_details())

expedition_3.assign_passenger(passenger_5)
expedition_3.assign_passenger(passenger_6)
# print(expedition_3.expedition_details())

# print(expedition_1.expedition_details()['passenger_list'][1].species)


# iterate over list of expeditions and print each one
for list in expedition_list:
    print(list.expedition_details())


# iterate over list of expeditions
# getting an expedition object
count = 1
for expedition in expedition_list:
    # use expedition details to access dictionary
    # get out origin, destination and ship, print in nice manner
    exp_details = expedition.expedition_details() # a dictionary
    print('Expedition number {}'.format(count))
    print('Origin:', expedition.get_origin())
    print('Destination:', expedition.get_destination())
    print('Spacecraft:', expedition.get_ship().identify_name())
    print('////////////////////////')
    count += 1

expedition_1.print_passenger_list()
expedition_2.print_passenger_list()
expedition_3.print_passenger_list()

# for list in expedition_list:
#         # iterate over passenger objects
#     for index in (list.expedition_details()):
#             # print out passenger details
#         print(index, list.expedition_details()[index])

# create while loop here

# use input() to get user input and generate objects dynamically

