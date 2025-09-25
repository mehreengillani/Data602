class Character:
  def __init__(self, name, role, power, ability, health=100):
    self.name = name
    self.role = role
    self.health = health
    self.power = power
    self.ability = ability

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Role: {self.role}")
    print(f"Health: {self.health}")
    print(f"Power: {self.power}")
    print(f"Ability: {self.ability}\n")

  def use_ability(self):
    print(f"{self.name} uses their special ability: {self.ability}!")

  def take_damage(self, amount):
  # If damage is negative or more than health → set health to 0
    if amount < 0 or amount >= self.health:
      self.health = 0
    else:
      self.health -= amount
    print(f"{self.name} took {amount} damage. Remaining health: {self.health}")

# Create characters
hero1 = Character("Alis", "Tank", 20, "Shield Wall")
hero2 = Character("David", "Damage", 35, "Fireball")

# Display info
hero1.display_info()
hero2.display_info()

# Use abilities
hero1.use_ability()
hero2.use_ability()

# Take damage
hero1.take_damage(30)
hero2.take_damage(-90)   # Health should not drop below 0
