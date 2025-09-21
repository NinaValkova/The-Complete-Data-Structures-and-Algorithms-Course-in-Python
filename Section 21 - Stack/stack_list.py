class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, element):
        self.data.append(element)    
                 
    def is_empty(self):
        return len(self.data) == 0
    
    def __str__(self):
        if self.is_empty():
            return 'Stack is empty'
        
        items = [str(value) for value in reversed(self.data)]    
        return '\n'.join(items)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.data.pop()
    
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.data[-1]
    
    def size(self):
        return len(self.data) 
    
    def clear(self):
        #self.data.clear()
        self.data = []
 
 
        
my_stack = Stack()

my_stack.push(4)        
my_stack.push(1)        
my_stack.push(6)        
my_stack.push(8)        
my_stack.push(4)    
my_stack.push(78)    

print(my_stack)
print()

my_stack.pop()
my_stack.pop()        

print(my_stack)
