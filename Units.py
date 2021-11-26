class Unit:
    """
    This class is a general class that applies to every unit in 40K.
    Every unit in the game has the follow infomation:
        name : stirng
            Name of the unit
        movement : int
            Inchs the model can move
        weaponSkill : int
            Chance to hit in melee
        ballisticSkill : int
            Chance to hit at range
        strength : int
            Strength in melee
        toughness : int
            Resistence to wounds
        wounds : int
            Number of hitpoints
        attacks : int
            Number of attacks in melee
        leadership : int
            Chance to runaway
        save : int
            Armour save
        role : [HQ, Troop, Fast Attack, Elite, Flyer, Heavy Support,
                    Fortification, Transport, Lord of War]
            The battlefield role for this unit
        power : int
            Power for this unit
        points : int
            Base point cost for unit
        centre : (int, int)
            x and y position of the centre of the unit in the game
        base : List((int,int))
    """
    
    def __init__(self, name, movement, weaponSkill, ballisticSkill, 
                 strength, toughness, wounds, attacks, leadership, save, role,
                 power, points, squadSize, transportCapacity, weapons):
        #Name of the unit for display purposes
        self.name = name
        
        #Define the stats of the unit
        self.movement = movement
        self.ws = weaponSkill
        self.bs = ballisticSkill
        self.s = strength
        self.t = toughness
        self.w = wounds
        self.a = attacks
        self.ld = leadership
        self.sv = save
        
        #Attributes for alive
        self.currentWounds = wounds
        self.alive = True
        
        #Define the type of unit
        self.role = role
        
        #Define the cost
        self.powerCost = power
        self.pointsCost = points
        self.squadSize = squadSize
        self.transportCapacity = transportCapacity
        self.weapons = weapons
        
        #Define the location of the unit on the map
        self.centre = (-1,-1)
        self.base = []
        
    def addOnetoSquad(self):
        self.squadSize += 1
        
    def addWeapon(self, Weapon):
        self.weapons.append(Weapon)
        
    def takeNormalDamage(self, damage):
        if damage >= self.currentWounds:
            self.squadSize -= 1
            self.currentWounds = self.wounds
            if self.squadSize == 0:
                self.alive = False
        else:
            self.currentWounds -= damage
    
    def totalPoints(self):
        return self.pointsCost * self.squadSize
    
    def moveUnit(self, newPosition):
        if ((newPosition[0] - self.centre[0])**2 
            + (newPosition[1] - self.centre[1])**2 <= self.movement**2):
            self.centre = newPosition
        else:
            print("Invalid move")
        
    def displayName(self):
        print("This unit is " + self.name)
        

class CircularBase(Unit):
    def __init__(self, name, movement, weaponSkill, ballisticSkill, 
                 strength, toughness, wounds, attacks, leadership, save, role,
                 power, points, squadSize, transportCapacity, weapons, diameter):
        
        #Define unit area
        self.diameter = diameter
        super().__init__(name, movement, weaponSkill, ballisticSkill, 
                 strength, toughness, wounds, attacks, leadership, save, role,
                 power, points, squadSize, transportCapacity, weapons)
        
class OvalularBase(Unit):
    def __init__(self, name, movement, weaponSkill, ballisticSkill, 
             strength, toughness, wounds, attacks, leadership, save, role,
             power, points, squadSize, transportCapacity, weapons, radius1, radius2):
        self.radius1 = radius1
        self.radius2 = radius2
        super().__init__(name, movement, weaponSkill, ballisticSkill, 
                 strength, toughness, wounds, attacks, leadership, save, role,
                 power, points, squadSize, transportCapacity, weapons)
    
class RectangularBase(Unit):
    def __init__(self, name, movement, weaponSkill, ballisticSkill, 
             strength, toughness, wounds, attacks, leadership, save, role,
             power, points, squadSize, transportCapacity, weapons, length, width):
        self.length = length
        self.width = width
        super().__init__(name, movement, weaponSkill, ballisticSkill, 
                 strength, toughness, wounds, attacks, leadership, save, role,
                 power, points, squadSize, transportCapacity, weapons)