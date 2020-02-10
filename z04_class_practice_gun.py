# 2/9/2020
# class practice
# class Gun

class Gun(object):
    def __init__(self, bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print("No more bullet")
        else:
            self.bulletBox.bulletCount -= 1
            print("Now bullet = %d" % self.bulletBox.bulletCount)