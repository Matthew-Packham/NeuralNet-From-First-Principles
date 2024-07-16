

### Create own Value object. It will represent data (just like say an interger) but will also have
### attributes that will be neccessary, such as .grad.
### IDEA: To build out the "expression graph" which represents the mathematical operations of a Neural Net


class Value:

    def __init__(self, data):
        self.data = data
    
    def __repr__(self) -> str:
        return f"Value(data={self.data})"
    
    def __add__(self, other):
        """
        Creates another Value object of the sum"""
        return Value(self.data + other.data)
    
    