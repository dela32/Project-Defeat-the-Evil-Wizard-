import random

# Base Character class

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.evaded = False

    def attack(self, opponent):
        damage = random.randint(10, 30)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Healing Method
    def heal(self):
        self.health = self.max_health
        return self.health
    
    def block(self): #  Dodge an attack
        self.evaded = True
        print(f"{self.name} has doged the attack")
            

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def attack(self, opponent):
        damage = random.randint(20, 35)
        opponent.health -= damage
        print(f"{self.name} swings their sword with {damage}")
        
        
    def special_ability(self, opponent): # Thousand Swords
        damage = self.attack_power + 50
        opponent.health -= damage
        print(f"{self.name} thousand swords to attack with {damage} attack power.")
    


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here
    def attack(self, opponent):
        damage = random.randint(20, 35)
        opponent.health -= damage
        print(f"{self.name} cast a spell with {damage}")
        
    def special_ability(self, opponent): #  Time Vortex
        damage = self.attack_power + 45
        opponent.health -= damage
        print(f"{self.name} time vortex to attack with {damage} attack power.")

    

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=25)
        
    def attack(self, opponent):
        damage = random.randint(20, 30)
        opponent.health -= damage
        print(f"{self.name} shoots their arrow with {damage}")
        
    def special_ability(self, opponent):  #   Quick Shot
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses quick shot to attack with {damage}.")

    def block(self): #   Evade
        print(f"{self.name} has evaded the attack")
        return True

        
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=35)
        
    def attack(self, opponent):
        damage = random.randint(20, 30)
        opponent.health -= damage
        print(f"{self.name} attacks with {damage}")
        
    def special_ability(self, opponent):      #   Holy Strike
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} used Holy Strike! {damage} Bonus Damage!")
        
    def block(self):    #   Divine Shield
        print(f"{self.name} used Divine Shield and has evaded the attack")
        return True
        
        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def attack(self, opponent):
        if opponent.evaded:
            print(f"{opponent.name} evaded the attack!")
            opponent.evaded = False  # Resets the evade status
        else:
            damage = random.randint(10, 25)
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            
            
# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Block")
        print("5. View Stats")
        
        choice = input("Choose an action: ")
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.block()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        
    if player.health <= 0:
        print(f"{player.name} has been defeated by {wizard.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()