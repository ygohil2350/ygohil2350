class Vehicle:
    def __init__(self,registration_number):
        self.registration_number=registration_number
    def run(self):
        print("The vehical is not running")
    def start(self):
        print("The vehical started")
    def stop (self):
        print("The vehical stopped")
class FourWheeler(Vehicle):
    def run(self):
        print("The four wheeler is running ")
        super().run()
    def stop(self):
        super().stop()
class Car(FourWheeler):
    def __init__(self,registration_number,is_commercial):
        super().__init__(registration_number)
        self.is_commercial=is_commercial
    def run(self):
        print("The car is running ")
        super().run()
    def start(self):
        print("the car started")
        if(self.is_commercial==True):
            super().run()
        else:
            super().start()
car=Car(3111,True)
car.start()

## output ##
#  the car started
#  The four wheeler is running 
#  The vehical is not running
