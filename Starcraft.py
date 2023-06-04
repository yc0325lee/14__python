# vim: ft=python ts=4 sw=4 tw=999 expandtab
# -*- coding:utf-8 -*-
# ----------------------------------------------------------------------------
# - file : Starcraft.py
# - author : yc0325lee
# - created : 2022-10-28 22:20:04 by lee2103
# - modified : 2022-10-28 22:20:04 by lee2103
# - description : 
# ; multiple inheritance
# ----------------------------------------------------------------------------

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[info] {0} is moving to location {1}. [speed= {2}]"
            .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        #super().__init__(name, hp)
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("[info] {0} unit created.".format(self.name), end=" ")
        print("hp= {0}, damage= {1}".format(self.hp, self.damage))

    def attack(self, location):
        print("[info] {0} is attacking location {1}!"\
            .format(self.name, location))

    def damaged(self, damage):
        print("[info] {0} has got {1} damage!"\
            .format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("[info] {0} was destroyed.".format(self.name))

class Flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self, name, location):
        print("[info] {0} is flying to location {1} [speed= {2}]!"\
            .format(name, location, self.speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, speed)


#marine1 = Unit("Marine", 40, 5)
#marine2 = Unit("Marine", 40, 5)
#tank = Unit("Tank", 150, 35)
#wraith1 = Unit("Wraith", 80, 5)
#wraith1.clocking = True

firebat = AttackUnit("Firebat", 50, 16, 3)
firebat.attack(5)
firebat.damaged(25)
firebat.damaged(25)

valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie.fly("Valkyrie", 3)
