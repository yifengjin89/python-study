# 2/9/2020
# class practice
# class Person

class Person(object):
    def __init__(self, gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def reloadBullet(self, count):
        self.gun.bulletBox.bulletCount = count
