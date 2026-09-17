class Tile:
    
    def __init__(self, Value):
        self.visited = False
        self.value = Value
        
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def is_visited(self):
        return self.visited
    
    def Visited(self):
        self.visited = True
