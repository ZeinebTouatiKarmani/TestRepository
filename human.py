class Human:

    def__init__(self):

        self.arms =1
        self.legs =2
        self.alive = True
        self.age = random.randint(1,100)


    def walk(self):

        print("is walking")

    def giveHug(self):
        if self.arms <2:
            print("no way")
        else:
            print ("hugging")


