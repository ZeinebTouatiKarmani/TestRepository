class Motor:

    def __init__(self):

        self.speed = 10     #attribut1
        self.acceleration =30  #attribut2
        self.maxSpeed =40  #attribut3
        self.pinA =69  #attribut4
        self.pinB =45  #attribut5


    def forward(self):   #method1
        print("forward")

    def reverse(self):  #method2
        print("reverse")


    def setSpeed(self):  #method3
        print("setSpeed")


    def x(self):   #method4
        print("x")

    def getMaxSpeed(self):
        return self.__maxSpeed

    def setMaxSpeed(speed):
        self.__maxSpeed=speed

