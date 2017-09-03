class Vehicle:
    def general_usage(self):
        print 'general use: transporation'

class Car(Vehicle):
    def __init__(self):
        print "i am car"
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print 'specific use: commute to work, vacation with family'

class MotoCycle(Vehicle):
    def __init__(self):
        print "i am motor cycle"
        self.wheels = 2
        self.has_roof = False

    def specific_use(self):
        print 'specific use: road trip, racing'

c = Car()
c.general_usage()
c.specific_usage()

m = MotoCycle()

#代码重用
#扩展性
#可读性

#isinstance方法和issubclass方法