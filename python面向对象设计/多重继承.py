# class Father():
#     def gardening(self):
#         print 'gardening, programming'
#
# class Mather():
#     def cooking(self):
#         print 'cooking, art'
#
# class Child(Father, Mather):
#     def sports(self):
#         print 'sports'
#
# c = Child()
# c.gardening()
# c.cooking()
# c.sports()
#
#
class Father():
    def skills(self):
        print 'gardening, programming'

class Mather():
    def skills(self):
        print 'cooking, art'

class Child(Father, Mather):
    def skills(self):
        Father.skills(self)
        Mather.skills(self)
        print 'sports'

c = Child()
c.skills()



