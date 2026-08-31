class node:

    def __init__(self,value):

        self.data = value
        self.next = None
        self.prev = None

class DoublyCircular:

    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0


    def InsertFirst(self,no):

        newn = node(no)

        if(self.first == None or self.last == None):

            self.first = newn
            self.last = newn

            self.last.next = self.first
            self.first.prev = self.last

        else:

            newn.next = self.first
            newn.prev = newn
            self.first = newn 

        self.first.prev = self.last
        self.last.next = self.first

        self.iCount= self.iCount+1


    def InsertLast(self,no):
        newn = node(no)

        if(self.first == None or self.last == None):

            self.first = newn
            self.last = newn

            self.last.next = self.first
            self.first.prev = self.last

        else:

            self.last.next = newn

            newn.prev = self.last 
            
            self.last = newn

        self.first.prev = self.last
        self.last.next = self.first

        self.iCount = self.iCount +1 


    def InsertAtPos(self,no,pos):

        
        if(pos < 1 or pos > self.iCount+1):

            print("Invalid Position")

            return

        if(pos == 1):

            self.InsertFirst(no)

        elif(pos == self.iCount+1):

            self.InsertLast(no)

        else:
            newn = node(no)

            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next


            newn.next = temp.next
            temp.next.prev = newn
            newn.prev = temp 
            temp.next = newn

            self.iCount = self.iCount+1

    def DeleteFirst(self):

        if(self.first == None or self.last == None):
            return
        elif(self.first == self.last):
            del self.first
            self.first = None
            self.last = None

        else:
            self.first = self.first.next

            self.first.prev = self.last 

            self.iCount = self.iCount -1


    def DeleteLast(self):
        if(self.first == None or self.last == None):
            return
        elif(self.first == self.last):
            del self.first
            self.first = None
            self.last = None

        else:

           self.last = self.last.prev
           del self.last.next

           self.last.next = self.first
           self.first.prev = self.last

        


        self.iCount = self.iCount -1


    def DeleteAtPos(self,pos):
        if(pos < 1 or pos > self.iCount+1):

            print("Invalid Position")

            return

        if(pos == 1):

            self.InsertFirst(no)

        elif(pos == self.iCount+1):

            self.InsertLast(no)

        else:

            temp = self.first 

            for i in range(1,pos-1):

                temp = temp.next


            temp.next = temp.next.next
            

            self.iCount = self.iCount-1


    def Display(self):

        temp = self.first

        while True:
            print("<-|",temp.data,"|->",end =" ")
            temp = temp.next

            if(temp == self.first):
                break

        print()

    def Count(self):

        return self.iCount
        



def main():

    sobj = DoublyCircular()

    sobj.InsertFirst(11)
    sobj.InsertFirst(21)
    sobj.InsertFirst(51)
    sobj.InsertFirst(101)

    print("The members of linked list are:")
    sobj.Display()
    print("The Count will be:",sobj.Count())


    sobj.InsertLast(111)
    sobj.InsertLast(222)
    sobj.InsertLast(333)
    sobj.InsertLast(444)

    print("The members of linked list are:")
    sobj.Display()
    print("The Count will be:",sobj.Count())


    sobj.InsertAtPos(123,3)

    print("The members of linked list are:")
    sobj.Display()
    
    print("The Count will be:",sobj.Count())


    sobj.DeleteFirst()
    print("The members of linked list are:")
    sobj.Display()
    
    print("The Count will be:",sobj.Count())

    sobj.DeleteLast()

    print("The members of linked list are:")
    sobj.Display()
    
    print("The Count will be:",sobj.Count())


    sobj.DeleteAtPos(2)

    print("The members of linked list are:")
    sobj.Display()
    
    print("The Count will be:",sobj.Count())














if __name__ == "__main__":
    main()