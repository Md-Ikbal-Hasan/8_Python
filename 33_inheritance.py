# super class
class Robot:
    def __init__(self,name,version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f"{self.name} is moving forward ! ")

    def move_backward(self):
        print(f"{self.name} is moving backward ! ")

    def move_right(self):
        print(f"{self.name} is moving right ! ")

    def move_left(self):
        print(f"{self.name} is moving left ! ")



# derived class/child class
class HouseBot(Robot):
    def __init__(self,name,version,area_covered):
        super().__init__(name, version) #Robot.__init__(name,version)
        self.area_covered = area_covered

    def clean(self):
        if self.area_covered > 0:
            print(f"{self.name} is cleaning the house. ")
            self.area_covered -= 30

            if self.area_covered < 0:
                self.area_covered = 0

        else:
            print(f"can not clean ! Pleae reset the area covered parameter")

    def set_cover_area(self,area):
        if self.area_covered == 0:
            self.area_covered = area
        else:
            print(f"I can still clean more area ! ")


    @staticmethod
    def halt():
        print("I am halting.")

    def move_forward(self):  # over ride the method.......
        print("This is in HouseBot Class.......")
        super().move_forward()



class MaidBot(HouseBot):
    def __init__(self,name,version,area_covered, cooking):
        super().__init__(name,version,area_covered)
        self.cooking = cooking






houseBot = HouseBot('Bob' , 1.1, 50)
robo = Robot('Stan lee'  ,1.5)


print(houseBot.name)
print(houseBot.version)
""" 
houseBot.move_forward()

houseBot.move_right()
houseBot.clean()
houseBot.clean()
houseBot.clean()
print(houseBot.area_covered)
houseBot.set_cover_area(50)
houseBot.clean()
houseBot.halt()
"""

'''
m = MaidBot('maidbot1' , 1.1 , 30 , 'biriyani')
print(m.name)
m.move_forward()
m.move_right()
m.clean()
m.clean()

'''


# interesting function............
""" 
#print(help(Robot))
#print(help(list))



print(issubclass(HouseBot , Robot))
print(issubclass(Robot , HouseBot))
print(issubclass(Robot , object))
print(issubclass(HouseBot , object))




print(isinstance(houseBot , Robot ))
print(isinstance(houseBot , HouseBot ))
print(isinstance(houseBot , object ))
print(isinstance(robo , object ))
"""
