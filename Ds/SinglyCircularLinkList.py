class node:

    def __init__(self,value):

        self.data = value
        self.next = None


class SinglyCl:

    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0


    def InsertFirst(self, no):
        newn = node(no)

        if(self.first == None or self.last == None):

            self.first = newn
            self.last = newn
            self.last.next = self.first

        else:
            newn.next = self.first
            self.first = newn

           

        self.last.next = self.first
        self.iCount = self.iCount+1
          


    def InsertLast(self,no):

        newn = node(no)
        if(self.first == None or self.last == None):
                self.first = newn
                self.last = newn
                self.last.next = self.first
        else:

            self.last.next = newn
            self.last = newn
            self.last.next = self.first

        self.iCount = self.iCount+1
            

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

            for i in range(1 , pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

        self.iCount = self.iCount+1


    def DeleteFirst(self):

        if(self.first == None or self.last == None):
            return

        else:

            self.first = self.first.next
            self.last.next = self.first

        self.iCount = self.iCount-1

    def DeleteLast(self):
        if(self.first == None or self.last == None):
            return

        else:
            temp = self.first 

            while(temp.next != self.last):
                temp = temp.next
  
            del self.last

            self.last = temp

            self.last.next = self.first

            self.iCount = self.iCount - 1

        

    def DeleteAtPos(self,pos):
        if(pos < 1 or pos > self.iCount):
            print("Invalid Position")
            return
        if(pos == 1):
            self.InsertFirst(no)
        elif(pos == self.iCount):
            self.InsertLast(no)
        else:
            temp = self.first 

            for i in range(1,pos-1):

                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount - 1


    def Display(self):

        temp = self.first

        while True:
            print("|",temp.data,"|->",end =" ")

            temp = temp.next

            if(temp == self.first):
                break

        print()

          

    def Count(self):
        return self.iCount
       


def main():
    
    sobj = SinglyCl()

    sobj.InsertFirst(11)
    sobj.InsertFirst(21)
    sobj.InsertFirst(51)
    sobj.InsertFirst(101)

    print("The link list will be")
    sobj.Display()

    print("Number in linked list are ",sobj.Count())


    sobj.InsertLast(122)
    sobj.InsertLast(133)
    sobj.InsertLast(144)
    sobj.InsertLast(155)

    print("The link list will be")
    sobj.Display()

    print("Number in linked list are ",sobj.Count())


    sobj.InsertAtPos(145,3)

    print("The link list will be")
    sobj.Display()

    print("Number in linked list are ",sobj.Count())


    sobj.DeleteFirst()


    print("The link list will be")
    sobj.Display()

    print("Number in linked list are ",sobj.Count())

    sobj.DeleteLast()

    print("The link list will be")
    sobj.Display()

    print("Number in linked list are ",sobj.Count())



    sobj.DeleteAtPos(2)


    print("The link list will be")
    sobj.Display()

    print("Number in linked list are ",sobj.Count())



if __name__ == "__main__":
    main()















        

