class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
LL1=linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(30)
LL1.print_LL()