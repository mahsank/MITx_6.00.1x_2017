'''
Write a method in Bag such that if b1 and b2 were bags then b1+b2 gives a new
bag representing the union of the two bags.

For example,
a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)
prints
3:1
4:2

'''

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
            self.vals[e] -= 1
        
    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)
    def __add__(self, other):
        from collections import Counter
        temp1 = Counter(self.vals)
        temp2 = Counter(other.vals)
        temp = temp1 + temp2
        s = ""
        for i,j in temp.items():
            s += str(i)+":"+str(j)+"\n"
        return s

