# 2/9/2020
# practice class ;

'''
Person
class name : Person
attribute ： gun
behavior ： fire

Gun
class name : Gun
attribute ： bulletBox
behavior ：  shoot

BulletBox
class name : BulletBox
attribute ： bullet
behavior ：  reload
'''

from z04_class_practice_person import Person
from z04_class_practice_gun import Gun
from z04_class_practice_bulletBox import BulletBox

# 弹夹
bulletBox = BulletBox(5)  # 装填子弹

# 枪
gun = Gun(bulletBox)  # 装填弹夹

# 人
person = Person(gun)  # 拿枪射击

person.fire()   # output： Now bullet = 4
person.fire()   # output： Now bullet = 3
person.fire()   # output： Now bullet = 2
person.fire()   # output： Now bullet = 1
person.fire()   # output： Now bullet = 0
person.fire()   # output： Now bullet = No more bullet
person.fire()   # output： Now bullet = No more bullet
person.reloadBullet(2)  # 重新装填子弹
person.fire()   # output： Now bullet = 1
person.fire()   # output： Now bullet = 0
person.fire()   # output： No more bullet
person.fire()   # output： No more bullet


