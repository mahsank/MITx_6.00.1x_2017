'''
Write a class that implements the specifications below. Do not override any
methods of Container.

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here

For example,
d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)
prints
4:2 # from d1.remove(2) print

    # (empty) from d1.remove(4) print
For example,
d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))
prints
True
True
False

'''

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals:
            self.vals.pop(e)
    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals:
            return True
        else:
            return False

