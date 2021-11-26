from Units import *
from Weapons import *

def guardianSpear():
    return [RangedWeapon("Guardian Spear (shooting)", 4, -1, 2, "-", 
                         24, ("R", 1)),
            MeleeWeapon("Guardian Spear (melee)", "+1", -3, "D3", "-")]           

def shieldCaptain():
    return CircularBase("Shield-Captain", 6,2,2,5,5,6,5,9,2, "HQ",
                        6, 100, 1, 0, guardianSpear(), 8)

def custodianGuard(squadSize):
    return CircularBase("Custodian Guard", 6,2,2,5,5,3,3,8,2, "Troop",
                        8, 40, squadSize, 0, guardianSpear(), 8)

def allarusCustodian(squadSize):
    return CircularBase("Allarus Custodians", 6,2,2,5,5,4,4,9,2, "Elite",
                        13, 70, squadSize, 0, guardianSpear(), 8)