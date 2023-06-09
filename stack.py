

class Stack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[-1]

# running time for each operation is O(1)
