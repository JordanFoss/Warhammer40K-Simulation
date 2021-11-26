class Army:
    def __init__(self):
        self.detachments = []
        self.points = 0
        self.power = 0
        
    def addDetachment(self, Detachment):
        self.detachments.append(Detachment)
        self.points += Detachment.pointsCost
        self.power += Detachment.powerCost
        
class Detachment:
    def __init__(self):
        self.HQs = []
        self.troops = []
        self.elites = []
        self.fastAttacks = []
        self.heavySupports = []
        self.flyers = []
        self.transports = []
        self.pointsCost = 0
        self.powerCost = 0
        
    def addHQ(self, Unit):
        if Unit.role == "HQ":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
        
    def addTroop(self, Unit):
        if Unit.role == "Troop":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
        
    def addElites(self, Unit):
        if Unit.role == "Elite":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
            
    def addFastAttack(self, Unit):
        if Unit.role == "Fast Attack":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
        
    def addHeavySupport(self, Unit):
        if Unit.role == "Heavy Support":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
        
    def addFlyer(self, Unit):
        if Unit.role == "Flyer":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
        
    def addTransports(self, Unit):
        if Unit.role == "Transport":
            self.HQs.append(Unit)
            self.pointsCost += Unit.totalPoints()
            self.powerCost += Unit.powerCost
        
    def removeHQ(self, Unit):
        self.HQs.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
        
    def removeTroop(self, Unit):
        self.troops.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
        
    def removeElites(self, Unit):
        self.elites.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
            
    def removeFastAttack(self, Unit):
        self.fastAttacks.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
        
    def removeHeavySupport(self, Unit):
        self.heavySupports.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
        
    def removeFlyer(self, Unit):
        self.flyers.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
        
    def removeTransports(self, Unit):
        self.transports.remove(Unit)
        self.pointsCost -= Unit.totalPoints()
        self.powerCost -= Unit.powerCost
        
    def isLegal(self):
        return ((len(self.HQs) <= self.HQsBounds[1] 
                and len(self.HQs) >= self.HQsBounds[0]) 
                and (len(self.troops) <= self.troopsBounds[1] 
                and len(self.troops) >= self.troopsBounds[0])
                and (len(self.elites) <= self.elitesBounds[1]
                and len(self.elites) >= self.elitesBounds[0])
                and (len(self.fastAttacks) <= self.fastAttacksBounds[1]
                and len(self.fastAttacks) >= self.fastAttacksBounds[0])
                and (len(self.heavySupports) <= self.heavySupportsBounds[1]
                and len(self.heavySupports) >= self.heavySupportsBounds[0])
                and (len(self.flyers) <= self.flyersBounds[1]
                and len(self.flyers) >= self.flyersBounds[0]))
        
class Patrol(Detachment):
    def __init__(self):
        super().__init__()
        self.HQsBounds = (1,2)
        self.troopsBounds = (1,3)
        self.elitesBounds = (0,2)
        self.fastAttacksBounds = (0,2)
        self.heavySupportsBounds = (0,2)
        self.flyersBounds = (0,2)
        self.commandCost = 2

class Battalion(Detachment):
    def __init__(self):
        super().__init__()
        self.HQsBounds = (2,3)
        self.troopsBounds = (3,6)
        self.elitesBounds = (0,6)
        self.fastAttacksBounds = (0,3)
        self.heavySupportsBounds = (0,3)
        self.flyersBounds = (0,2)
        self.commandCost = 3
    
class Brigade(Detachment):
    def __init__(self):
        super().__init__()
        self.HQsBounds = (3,5)
        self.troopsBounds = (6,12)
        self.elitesBounds = (3,8)
        self.fastAttacksBounds = (3,5)
        self.heavySupportsBounds = (3,5)
        self.flyersBounds = (0,2)
        self.commandCost = 4
    
class Vanguard(Detachment):
    def __init__(self):
        super().__init__()
        self.HQsBounds = (1,2)
        self.troopsBounds = (0,3)
        self.elitesBounds = (3,6)
        self.fastAttacksBounds = (0,2)
        self.heavySupportsBounds = (0,2)
        self.flyersBounds = (0,2) 
        self.commandCost = 3

class Spearhead(Detachment):
    def __init__(self):
        super().__init__()
        self.HQsBounds = (1,2)
        self.troopsBounds = (0,3)
        self.elitesBounds = (0,2)
        self.fastAttacksBounds = (0,2)
        self.heavySupportsBounds = (3,6)
        self.flyersBounds = (0,2)
        self.commandCost = 3
        
class Outrider(Detachment):
    def __init__(self):
        super().__init__()
        self.HQsBounds = (1,2)
        self.troopsBounds = (0,3)
        self.elitesBounds = (0,2)
        self.fastAttacksBounds = (3,6)
        self.heavySupportsBounds = (0,2)
        self.flyersBounds = (0,2)
        self.commandCost = 3
