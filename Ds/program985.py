class node:

    def __init__(self,value):

        self.data = value
        self.next = None

def main():

    head = None 

    obj1 = node(11)
    obj2 = node(21)
    obj3 = node(51)
    obj4 = node(101)

    head = obj1
    head.next = obj2
    obj2.next = obj3
    obj3.next = obj4
    obj4.next = None
    temp = head

    while(temp != None):
        print("|",temp.data,"|->",end =" ")
        temp = temp.next

    print("None")
        
   
    

if __name__ == "__main__":

    main()


