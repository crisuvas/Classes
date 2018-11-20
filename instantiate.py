class Hero(object):

    classification = "Hero"

    def __init__(self, weapon, shield, super_power):
        self.weapon = weapon
        self.shield = shield
        self.super_power = super_power

    def equipment_check(self):
        if self.weapon != "" or self.shield:
            return "You have some equipment"
        elif self.weapon != "" and self.shield:
            return "You have a nice equipment"
        else:
            return "You need to get some equipment"

    def use_super_power(self):
        if self.super_power != "":
            return "I will use %s" % self.super_power
        else:
            return "I don'n have a super power to use"


cris = Hero("Sword", True, "Giga Explotion")
jaimito = Hero("", False, "")
print(cris.equipment_check())
print(jaimito.equipment_check())
print(cris.use_super_power())
