class GameObject():
    def __init__(self, created_at, name, dimensions):
        self.created_at = created_at
        self.name = name
        self.dimensions = dimensions

    def destroy(self):
        return f'{self.name} was removed from the game'


class CharacterStats(GameObject):
    def __init__(self, health_points):
        self.health_points = health_points

    def take_damage(self):
        return f'{self.name} took damage'


class Humanoid(CharacterStats):
    def __init__(self, created_at, name, dimensions, health_points, team, weapons, language):
        CharacterStats.__init__(self, health_points)
        GameObject.__init__(self, created_at, name, dimensions)
        self.team = team
        self.weapons = weapons
        self.language = language

    def greet(self):
        return f'{self.name} offers a greeting in {self.language}'


mage = Humanoid('now', 'Bruce', {'length': 2, 'width': 1, 'height': 1}, 5, 'Mage Guild', ['Staff of Shamalama'],
                'Common Tounge');
swordsman = Humanoid('now', 'Sir Mustachio', {'length': 2, 'width': 2, 'height': 2}, 15, 'The Round Table',
                     ['Giant Sword', 'Shield'], 'Common Tounge');
archer = Humanoid('now', 'Lilith', {'length': 1, 'width': 2, 'height': 4}, 10, 'Forest Kingdom', ['Bow', 'Dagger'],
                  'Elvish');

print(mage.created_at)
print(archer.dimensions)
print(swordsman.health_points)
print(mage.name)
print(swordsman.team)
print(mage.weapons)
print(archer.language)
print(archer.greet())
print(mage.take_damage())
print(swordsman.destroy())
