class Demo
{
    public int Factorial(int No)
    {
        if (No == 0)
        {
            return 1;

        }
        return No * Factorial(No-1);
    }
}


class program998
{
    public static void main(String A[])
    {
        Demo.dobj = new Demo();

        int iRet = 0;

        iRet = dobj.Factorial();

        System.out.println("Factor are",iRet);
        
    
    }
}