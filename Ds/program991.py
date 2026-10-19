class ArrayX:

     def __init__(self,size):
        self.size = size
        self.Arr = [0] * size

     def Accept(self):

        print("Enter they elements:")

        for i in range(self.size):

            value = int(input())
            self.Arr[i] = value

     def Display():

         print("Elements of they array are:")

         for i in range(self.size):

            print(self.Arr[i])

    
     def Summation():

        iSum =0

        print("Elements of they array are:")

        for i in range(self.size):

            iSum = iSum + self.Arr[i]

        return iSum

            

       





def main():

    aobj = ArrayX(5)

    aobj.Accept()

    aobj.Display()

    Ret = sobj.Summation()

    print("Summation is:",Ret)

if __name__ == "__main__":
    main()

