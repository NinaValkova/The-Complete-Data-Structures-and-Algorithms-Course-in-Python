# both start and top move around the array, wrapping back to 0 when they hit the end; (front = start, rear = top):
#Example
# Step 1 : enqueue 5 items
# Q = Queue(5)
# Q.enqueue("A")
# Q.enqueue("B")
# Q.enqueue("C")
# Q.enqueue("D")
# Q.enqueue("E")
# data  is [A, B, C, D, E]
# start = 0
# top   = 4

# Step 2: dequeue 2 items
# Q.dequeue() 
# Q.dequeue()  
# data is [None, None, C, D, E]
# start = 2   
# top   = 4        


class Queue:
    def __init__(self, max_size):
        self.data = [None]*max_size
        self.max_size = max_size
        self.top = -1 # index of the rear element
        self.start = -1 # index of the front element
    
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
                return True
        return False    
    
    def enqueue(self, element):
        if self.is_full():
            return 'Queue is full'
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else: 
                if self.top == -1:
                    self.start = 0   
                self.top += 1
                
            self.data[self.top] = element
            
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            first_element = self.data[self.start]
            start = self.start
            
            if self.start == self.top: # only 1 element in the queue - Queue: [None, None, A, None, None] start = 2, top = 2; After dequeue, the queue becomes empty → so you reset both pointers to -1.
                self.start = -1
                self.top - -1
            elif self.start + 1 == self.max_size: # self.start is pointing at the last slot of the list, but there are still elements left after wrap-around. Queue: [B, C, None, None, A]; start = 4  (pointing to A, the oldest element) and  top = 1(pointing to C, the newest element)
                self.start = 0
            else: 
                self.start += 1    
            
            self.data[start] = None
            return first_element    
        
    def peek(self):
        if self.is_empty():
            return 'Queue is empty' 
        return self.data[self.start]
    
    def delete(self):
        self.data = [None] * self.max_size
        self.start = -1
        self.top = -1
        
    def __str__(self):
        if self.is_empty():
            return 'Queue is empty'
        
        items = [str(item) for item in self.data]   
        return ' '.join(items)         
        
            
my_queue = Queue(10)

my_queue.enqueue(4)
my_queue.enqueue(1)
my_queue.enqueue(6)
my_queue.enqueue(8)
my_queue.enqueue(4)
my_queue.enqueue(78)
    
print(my_queue)
print()

my_queue.dequeue()
my_queue.dequeue()

print(my_queue)
    

