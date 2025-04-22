class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin
        self.__energy = 100  # Encapsulated attribute

    def use_power(self):
        if self.__energy >= 10:
            self.__energy -= 10
            return f"{self.name} uses {self.power}! 💥 Energy left: {self.__energy}"
        else:
            return f"{self.name} is too tired to use their power. 💤"

    def recharge(self):
        self.__energy = 100
        return f"{self.name} has recharged to full energy! 🔋"

    def get_status(self):
        return f"🦸‍♂️ {self.name} | Power: {self.power} | Origin: {self.origin} | Energy: {self.__energy}"


class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h! 🕊️"


# Interactive mode
if __name__ == "__main__":
    print("Welcome to the Superhero Creator! 🦸")
    name = input("Enter superhero name: ")
    power = input("Enter superhero power: ")
    origin = input("Where is your superhero from? ")
    flight_speed = int(input("What is your superhero's flight speed (km/h)? "))

    hero = FlyingSuperhero(name, power, origin, flight_speed)

    print("\nHero Created Successfully!\n")
    print(hero.get_status())
    print(hero.use_power())
    print(hero.fly())
    print(hero.recharge())
    print(hero.get_status())
