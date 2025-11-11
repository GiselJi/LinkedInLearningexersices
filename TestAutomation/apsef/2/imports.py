import time
import pytest
from classes import Motorcycle, Car

print(Motorcycle) # tells what Motorcycle is from classes file

moto = Motorcycle('Triumph', 'Thruxton') #Creating a new instance of a class
car = Car('Honda', 'Civic')

for vehicles in [moto, car]:
    print(f'The time is {time.time()}')
    print(vehicles) #Prints mem address of the instance if no __repr__ defined 

    vehicles.turn_engine_on()
    vehicles.turn_headligh_on()
    vehicles.start_driving()
    vehicles.turn('left')
    vehicles.turn('right')
    vehicles.stop_driving()
    vehicles.turn_engine_off()
    vehicles.turn_headlight_off()
    print()
    time.sleep(1) #sleep program for 1 second