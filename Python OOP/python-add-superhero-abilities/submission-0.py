class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        """ initialize a superhero object. """
        self.name = name
        self.power = power
        self.health = health
    

    # TODO: Define attack method and implement it
    def attack(self):
        """ Prints out stating that a certain superhero attacked with its own specific power. """
        print(f"{self.name} attacks with {self.power}!")

    # TODO: Define heal method and implment it
    def heal(self):
        """ Increases the superhero health attribute by 10 and prints out a statement about it. """
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")
     

# TODO: Create superhero instance
catwoman = SuperHero("Catwoman", "Agility", 120)


# TODO: Use the attack() and heal() method
catwoman.attack()
catwoman.heal()