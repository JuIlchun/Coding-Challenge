package Euler.java;

public class euler1
{
    static public void main(String[] args)
    {
        int ans=0;
        for (int i=0;i<1000;i++)
        {
            if (i%3==0)
            {
                ans+=i;
            }
            else if (i%5==0)
            {
                ans+=i;
            }
        }
        System.out.println(ans);
    }
}
