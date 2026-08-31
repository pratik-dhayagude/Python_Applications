class node:

    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:

    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self,no):

        newn = node(no)

        if(self.first == None):
            self.first = newn
        else:
            newn.next = self.first 
            self.first.prev = newn
            self.first = newn

        self.iCount = self.iCount + 1


    def InsertLast(self,no):

        newn = node(no)

        if(self.first == None):

            self.first = newn

        else:

            temp = self.first 

            while(temp.next != None):
                temp = temp.next

            temp.next = newn 
            newn.prev = temp 
            newn.next = None


        self.iCount = self.iCount + 1


    def InsertAtPos(self,no,pos):

        if(pos < 1 or pos > self.iCount+1):

            print("Invalid Position")

            return

        if(pos == 1):

            self.InsertFirst(no)

        elif(pos == self.iCount+1):

            self.InsertLast(no)

        else:

            temp = self.first

            newn = node(no)

            for i in range(1,pos-1):

                temp = temp.next 

            newn.next = temp.next
            temp.next.prev = newn
            newn.prev = temp
            temp.next = newn

            self.iCount = self.iCount+1



    def DeleteFirst(self):

        if(self.first == None):

            return

        else:

            self.first = self.first.next

        self.iCount = self.iCount -1

    def DeleteLast(self):
        if(self.first == None):
            return
        else:

            temp = self.first 

            while(temp.next.next != None):

                temp = temp.next

            temp.next = None

        self.iCount = self.iCount -1    


    def DeleteAtPos(self,pos):

        if(pos<1 or pos > self.iCount):

            print("Invalid Position")
            return

        if(pos == 1):

            self.DeleteFirst()

        elif(pos == self.iCount):

            self.DeleteLast()

        else:

            temp = self.first 

            for i in range(1,pos-1):
                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount-1




    def Display(self):

        temp = self.first 

        while(temp.next != None):
            print("<-|",temp.data,"|->",end =" ")
            temp = temp.next

        print()

        


    def Count(self):
        return self.iCount


def main():

    sobj = DoublyLL()

    sobj.InsertFirst(11)
    sobj.InsertFirst(21)
    sobj.InsertFirst(51)
    sobj.InsertFirst(101)


    print("Data from the link list will be :")

    sobj.Display()

    print("The Count will be:",sobj.Count())



    sobj.InsertLast(111)
    sobj.InsertLast(222)
    sobj.InsertLast(333)
    sobj.InsertLast(333)

    print("Data from the link list will be :")

    sobj.Display()

    print("The Count will be:",sobj.Count())


    sobj.InsertAtPos(123,3)

    print("Data from the link list will be :")

    sobj.Display()


    print("The Count will be:",sobj.Count())


    sobj.DeleteFirst()

    print("Data from the link list will be :")

    sobj.Display()


    print("The Count will be:",sobj.Count())

    sobj.DeleteLast()

    print("Data from the link list will be :")

    sobj.Display()


    print("The Count will be:",sobj.Count())


    sobj.DeleteAtPos(2)

    print("Data from the link list will be :")

    sobj.Display()


    print("The Count will be:",sobj.Count())


















if __name__ == "__main__":

    main()