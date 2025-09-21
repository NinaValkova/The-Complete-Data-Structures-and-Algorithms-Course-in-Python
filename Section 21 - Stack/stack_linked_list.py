class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
    
    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        
        popped_node = self.top
        self.top = popped_node.next
        popped_node.next = None
        self.length -= 1  
        
        return popped_node
    
    def peek(self):
        return self.top.value
    
    def is_empty(self):
        return self.length == 0
    
    def __str__(self):
        if self.is_empty():
            return 'Stack is empty'
        
        items = []
        current = self.top
        while current:
            items.append(str(current.value))
            current = current.next
            
        return '\n'.join(items)
    
    def clear(self):
        self.top = None
        self.length = 0
     
     
        
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
    
        
                    