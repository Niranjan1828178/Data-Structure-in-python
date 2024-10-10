import time
class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            return
        tem=self.head
        while tem.next is not None:
            tem=tem.next
        tem.next=newnode
        newnode.prev=tem

    
    def insert_at_start(self,data):
        newnode=node(data)
        if not self.head:
            self.head=newnode
            return
        
        tem=self.head
        newnode.next=tem
        self.head=newnode
        tem.prev=newnode

    
    def delete_at_end(self):
        if not self.head:
            time.sleep(1)
            print('list is empty!')
            print()
            return
        if self.head.next is None:
            time.sleep(1)
            print('deleted node is: ',self.head.data)
            print('list is now empty!')
            print()
            self.head=None
            return
        time.sleep(1)
        tem=self.head
        while tem.next is not None:
            tem=tem.next
        print('deleted node is: ',tem.data)
        print()
        tem.prev.next=None
        tem.prev=None
        

    def print(self):
        if not self.head:
            time.sleep(1)
            print('list is empty!')
            print()
            return
        time.sleep(1)
        tem=self.head
        while tem is not None:
            print(tem.data,end='<->')
            tem=tem.next
        print('None')
        print()
        
    
    def length(self):
        count=0
        if self.head:
            tem=self.head
            while tem is not None:
                tem=tem.next
                count+=1
            time.sleep(1)
            return count
        

    def get_previous_node(self,data1):
        if not self.head:
                time.sleep(1)
                print('list is empty!')
                print()
                return
        if self.head.next is None:
                time.sleep(1)
                print('list has only one item that is: ',self.head.data)
                print()
                return
        
        tem=self.head.next
        while tem is not None:
            if tem.data==data1:
                time.sleep(1)
                print('previous of ',data1,' is: ',(tem.prev).data)
                print()
                return
            tem=tem.next
        time.sleep(1)
        print(data1,' is not in list')
        print()

    def print_reverse(self):
        if not self.head:
            time.sleep(1)
            print('list is empty!')
            print()
            return
        if self.head.next is None:
            time.sleep(1)
            print(self.head.data,'<->None')
            print()
            return
        time.sleep(1)
        tem=self.head
        while tem.next is not None:
            tem=tem.next
        print('None',end='<-')
        while tem is not None:
            print('>',tem.data,end='<-')
            tem=tem.prev
        print('start')
        print()
        

    def delete_at_start(self):
        if not self.head:
            time.sleep(1)
            print('list is empty!')
            print()
            return
        if self.head.next is None:
            time.sleep(1)
            print('deleted item is: ',self.head.data)
            print('list is now empty!')
            print()
            self.head=None
            return
        time.sleep(1)
        print('deleted item is: ',self.head.data)
        print()
        tem=self.head.next
        self.head=tem
        tem.prev=None
        

dl=DoubleLinkedList()
print('welcom to DOUBLE LINKED LIST...')
while True:
    print('1: insert at end')
    print('2: insert at start')
    print('3: delete at end')
    print('4: delete at start')
    print('5: get previous node')
    print('6: print list')
    print('7: print list in reverse order')
    print('8: get length of list')
    choice=input('enter your choice: ')
    if choice=='1':
        dl.insert_at_end(int(input('enter a number to insert: ')))
        
    elif choice=='2':
        dl.insert_at_start(int(input('enter a number to insert: ')))
        
    elif choice=='3':
        dl.delete_at_end()
        
    elif choice=='4':
        dl.delete_at_start()
        
    elif choice=='5':
        dl.get_previous_node(int(input('enter the current data: ')))
    
    elif choice=='6':
        dl.print()
        
    elif choice=='7':
        dl.print_reverse()
    
    elif choice=='8':
        print('number of elements in the list are: ',dl.length())
        print()

    elif choice=='9':
        exit()

    else:
        print('Invalid choice, please try again\n')
