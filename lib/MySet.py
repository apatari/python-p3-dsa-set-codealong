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
    
    def __str__(self):
        set_string = "MySet: {"
        for key in self.dictionary:
            set_string += f'{key},'
        
        set_string = set_string[:-1]
        set_string += "}"
        if self.size() == 0:
            return "MySet: {}"

        return set_string
    
    def clear(self):
        self.dictionary = {}
        return self.dictionary

    
test_set = MySet([1,2,3])

print(test_set)

test_set.clear()

print(test_set.size())

print(test_set)

    
