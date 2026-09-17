class Tile:
    
    def __init__(self, Value):
        self.visited = False
        self.value = Value
        self.safety = True
        
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        self.safety = (value != 9)
    
    def is_visited(self):
        return self.visited
    
    def Visited(self):
        self.visited = True

    def is_safe(self):
        return self.safety
