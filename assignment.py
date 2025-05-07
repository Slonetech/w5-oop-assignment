# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and my power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flying_speed):
        super().__init__(name, power, origin)
        self.flying_speed = flying_speed

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flying_speed} km/h using {self.power}!")

# Another inherited class
class StrengthSuperhero(Superhero):
    def __init__(self, name, power, origin, strength_level):
        super().__init__(name, power, origin)
        self.strength_level = strength_level

    def use_power(self):
        print(f"{self.name} lifts objects weighing up to {self.strength_level} tons with {self.power}!")

# Creating objects
hero1 = FlyingSuperhero("Skyhawk", "Flight", "Metro City", 900)
hero2 = StrengthSuperhero("Titan", "Super Strength", "Gotham", 200)

hero1.introduce()
hero1.use_power()
hero2.introduce()
hero2.use_power()
