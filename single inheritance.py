#super class

class _Shape:
    _length = None
    _breadth = None
    
    def _getdata(self, length, breadth):
        self._length = length
        self._breadth = breadth


#derived class
        
class rectangle(_Shape):
    
    def display(self):
        print("area of rectangle:",self._length * self._breadth)


obj = rectangle()
obj._getdata(4, 4)
obj.display()
