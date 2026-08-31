
#finalcode of singly linked list
class node:

    def __init__(self,value):

        self.data = value
        self.next = None

class SinglyLL:

    #done
    def __init__(self):

        self.first = None
        self.iCount = 0

    #done
    def InserFirst(self,no):
        nobj = node(no)

        if(self.first == None):

            self.first = nobj

        else:

            nobj.next = self.first
            self.first = nobj

        self.iCount = self.iCount + 1
    
       
    #done
    def InserLast(self,no):
        newn = node(no)

        if(self.first == None):
            self.first = nobj

        else:

            temp = self.first
            while(temp.next != None):
                temp = temp.next

            temp.next = newn
              
        self.iCount = self.iCount + 1

        
    def InserAtPos(self,no,pos):
        if(pos == 1):

            self.InserFirst(no)
            return

        elif(pos == self.iCount+1):

            self.InserLast(no)
            return

        else:
            newn = node(no)

            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next 

            newn.next = temp.next 
            temp.next = newn


            self.iCount = self.iCount + 1   

    def DeleteFirst(self):

        temp = self.first

        if(self.first == None):

            return 

        else:

            self.first = self.first.next
            del temp

            self.iCount = self.iCount - 1



    def DeleteLast(self):
        if(self.first == None):

            return
        else:

            temp = self.first

            while(temp.next.next != None):

                temp = temp.next

        temp.next = None

        self.iCount = self.iCount - 1


    
    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > (self.iCount)):

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

            


        temp .next = temp.next.next
        self.iCount = self.iCount - 1




    def Display(self):

        temp = self.first 

        while(temp != None):

            print("|",temp.data,"|->",end =" ")
            temp = temp.next

        print("None")
        
      

    #done
    def Count(self):

        return self.iCount


      
        
def main():

    sobj = SinglyLL()

    sobj.InserFirst(11)
    sobj.InserFirst(21)
    sobj.InserFirst(51)
    sobj.InserFirst(101)


    print("Elements of link list")
    sobj.Display()

    print("Number of link list is ",sobj.Count())

    sobj.InserLast(111)
    sobj.InserLast(121)
    sobj.InserLast(151)
    sobj.InserLast(191)

    print("Elements of link list")
    sobj.Display()

    print("Number of link list is ",sobj.Count())


    sobj.InserAtPos(123,4)

    print("Elements of link list")
    sobj.Display()

    print("Number of link list is ",sobj.Count())


    sobj.DeleteFirst()

    print("Elements of link list")
    sobj.Display()

    print("Number of link list is ",sobj.Count())


    sobj.DeleteLast()

    print("Elements of link list")
    sobj.Display()

    print("Number of link list is ",sobj.Count())

    sobj.DeleteAtPos(2)

    print("Elements of link list")
    sobj.Display()

    print("Number of link list is ",sobj.Count())



    
if __name__ == "__main__":

    main()