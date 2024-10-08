class Stack:
    
    
    stack=[]
    top=-1
    def push(self,value):
        self.top = self.top + 1
        self.stack.append(value)
    
    def pop(self):
        if self.top < 0:
            print("Stack is empty")
            return
        else:
            print("pop " , self.stack[self.top])
            self.top -= 1
            self.display()
            return 

    def is_empty(self):
        if self.top <0:
            return True
        else:
            return False
    
    def display(self):
        if self.top <0:
            print("Stack is empty")
            return
        print('stack elements are: ',end='')
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=" ")
        print()

s=Stack()
print('welcome to Stack operations')

while True:
    print('1. Push')
    print('2. Pop')
    print('3. is_empty')
    print('4. Display')
    print('5. Exit')
    choice = input('Enter your choice: ')
    
    if choice =='1':
        value = int(input('Enter the value to push: '))
        s.push(value)
        
    elif choice=='2':
        s.pop()

    elif choice=='3':
        print(s.is_empty())
        
    elif choice=='4':
        s.display()
        
    elif choice=='5':
        exit('thank you for using Stack')
    
    else:
        print('Invalid choice!, please try again\n')


