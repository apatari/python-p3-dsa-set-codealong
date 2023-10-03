class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for val in enumerable:
            self.dictionary[val] = True

    def has(self,value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)

    
