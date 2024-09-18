class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
        
    # Iterator        
    def __iter__(self):
        self.data = [{'length': self.length}, {'width': self.width}]
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
rectangle = Rectangle(10, 5)

for attribute in rectangle:
    print(attribute)                        