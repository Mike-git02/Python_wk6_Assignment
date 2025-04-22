from superhero import Superhero, FlyingSuperhero

def get_valid_input(prompt, type_=str, valid_range=None):
    """Helper function to validate user input"""
    while True:
        try:
            value = type_(input(prompt))  # Try converting input to the desired type
            if valid_range and value not in valid_range:
                print(f"Invalid input! Please enter one of {valid_range}.")
                continue
            return value
        except ValueError:
            print(f"Invalid input! Please enter a valid {type_.__name__}.")

def main():
    """Main function to interact with the user and create superheroes"""
    print("Welcome to the Superhero Creator!\n")
    
    # Get user input for superhero details
    name = input("Enter your superhero's name: ")
    power = input("Enter your superhero's special power: ")
    energy = get_valid_input("Enter your superhero's energy (0-10): ", int, range(0, 11))

    # Create a Superhero or FlyingSuperhero based on user choice
    superhero_choice = input("Would you like your superhero to fly? (yes/no): ").lower()
    
    if superhero_choice == "yes":
        flight_speed = get_valid_input("Enter flight speed (1-10): ", int, range(1, 11))
        superhero = FlyingSuperhero(name, power, energy, flight_speed)
        print(f"\nCreated a FlyingSuperhero named {name}!")
    else:
        superhero = Superhero(name, power, energy)
        print(f"\nCreated a Superhero named {name}!")

    # Show the superhero's status and interact
    superhero.get_status()

    # Demonstrate superhero actions
    superhero.move()
    superhero.rest()
    superhero.get_status()

    # Polymorphism: calling move() on FlyingSuperhero or Superhero
    if isinstance(superhero, FlyingSuperhero):
        superhero.fly()  # Flying action for flying superhero

if __name__ == "__main__":
    main()
