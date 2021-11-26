class Weapon:
    def __init__(self, name, strength, ap, damage, abilities):
        self.name = name
        self.strength = strength
        self.ap = ap
        self.damage = damage
        self.abilities = abilities
        
    def displayName(self):
        print(self.name)
        
class RangedWeapon(Weapon):
    
    def __init__(self, name, strength, ap, damage, abilities, Range, Type):
        super().__init__(name, strength, ap, damage, abilities) 
        
        self.Range = Range
        # Type is a 2 tuple with A,H,R,G,P for the first term
        # and int for the second
        self.Type = Type


class MeleeWeapon(Weapon):
    def __init__(self, name, strength, ap, damage, abilities):
        super().__init__(name, strength, ap, damage, abilities) 