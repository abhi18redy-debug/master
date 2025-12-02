class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        if self.head.next:
            last = self.head.next
        last.next = new_node
        new_node.prev = last
        
        
    def forward_display(self):
        current = self.head
        print('forward')
        while current: 
            print("{} -> ".format(current.data) )
            if current.next:
                current = current.next
            else:
                return current
            
    def backward_display(self):
        current = self.forward_display()
        print('backward')
        while current: 
            print("{} -> ".format(current.data) )
            current = current.prev
            
            
    def del_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
            
        return False
        
        
obj = linkedlist()
obj.append(100)
obj.append(200)
obj.append(300)


obj.backward_display() 
obj.del_value(200)   

obj.backward_display()         