class Queue:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        if self.data == []:
            return True
        return False   
    
    def enqueue(self, element):
        self.data.append(element) 
        
    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty' 
        return self.data.pop(0)       
    
    def peek(self):
        if self.is_empty():
            return 'Queue is empty' 
        return self.data[0]
    
    def delete(self):
        # self.data = None destroys the queue (can’t use it again) - removes the list and replaces it with None
        self.data = [] #   empties the queue (you can keep using it).
    
    def __str__(self):
        if self.is_empty():
            return 'Queue is empty'
        
        items = [str(item) for item in self.data]   
        return ' '.join(items) 
    
my_queue = Queue()

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
    
    