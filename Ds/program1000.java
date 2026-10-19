class Demo
{
    void Display(int No)
    {
        if (No == 0)
        {
            return ;

        }
        System.out.println(No);
        Display(No-1);
        System.out.println(No);
    }
}
class program1000
{
    public static void main(String A[])
    {
        Demo dobj = new Demo();

        int iRet = 0;

        dobj.Display(5);
    }
}