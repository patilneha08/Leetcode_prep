class Node:
        
        def __init__(self,key,val,next=None,prev=None):
            self.key=key
            self.val=val
            self.next=next
            self.prev=prev

class LRUCache:

    def __init__(self, capacity: int):

        self.head=Node(-1,-1)
        self.tail=Node(-1,-1,None,self.head)
        self.head.next=self.tail
        self.cap=capacity
        self.map={}

    def delete(self,node):
        temp1=node.prev
        temp2=node.next
        temp1.next=temp2
        temp2.prev=temp1

    def insert(self,node):
        temp=self.head.next
        node.prev=self.head
        node.next=temp
        temp.prev=node
        self.head.next=node

    def get(self, key: int) -> int:
        if key in self.map:
            self.delete(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val=value
            self.delete(self.map[key])
            self.insert(self.map[key])
        else:
            if len(self.map)==self.cap:
                temp=self.tail.prev.key
                self.delete(self.tail.prev)
                del self.map[temp]
                self.map[key]=Node(key,value)
                self.insert(self.map[key])
            else:
                self.map[key]=Node(key,value)
                self.insert(self.map[key])
        return None