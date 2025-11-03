class Vehicle:
    is_engine_on = False
    is_headlight_on = False
    make = None
    model = None
    is_driving = False

    def __init__(self, make, model): #Magic method, inits instance for us
        self.make = make
        self.model = model

    def __repr__(self): #Magic method, represents our instance as a string
        return (f'{self.make} {self.model} with engine '
                f'{" on " if self.is_engine_on else " off "}'
                f'and headligh {" on " if self.is_headlight_on else " off "}')

    def turn_engine_on(self):#Function inside a class is a method
        print("Turning engine on")
        self.is_engine_on = True

    def turn_engine_off(self):
        print("Turning engine off")
        if self.is_driving:
            print("Can't turn off engine while driving")
            return
        self.is_engine_on = False

    def turn_headligh_on(self):
        print("Turning headlights on")
        self.is_headlight_on = True

    def turn_headlight_off(self):
        print("Turning healdlights off")
        self.is_headlight_on = False

    def start_driving(self):
        if not self.is_engine_on:
            print("You can't drive without turning the engine on!")
            return
        
        print("Starting to drive")
        self.is_driving = True

    def stop_driving(self):
        print("Stopping")
        self.is_driving = False

class Motorcycle(Vehicle): #Creating a class(abstract idea of an object)
    def lean(self, direction):
        if not self.is_driving:
            print("You leaned while not driving, motorcycle fell")
            return

        print(f'Leaning {direction}')

    def turn_handlebars(self, direction):
        print(f'Turning handlebars {direction}')

    def turn(self, direction):
        if direction == 'left':
            self.turn_handlebars('right')
            self.lean('left')
        elif direction == 'right':
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Did not understand direction")

class Car(Vehicle): #Creating a class(abstract idea of an object)
    def turn_steering_wheel(self, direction): 
        print(f'Turning steering wheel {direction}')

    def turn(self, direction):
        if direction in ['left', 'right']:
            self.turn_steering_wheel(direction)
        else:
            print("Did not understand direction")

moto = Motorcycle('Triumph', 'Thruxton') #Creating a new instance of a class
car = Car('Honda', 'Civic')

for vehicles in [moto, car]:
    print(vehicles) #Prints mem address of the instance if no __repr__ defined 

    vehicles.turn_engine_on()
    vehicles.turn_headligh_on()
    vehicles.start_driving()
    vehicles.turn('left')
    vehicles.turn('right')
    vehicles.stop_driving()
    vehicles.turn_engine_off()
    vehicles.turn_headlight_off()