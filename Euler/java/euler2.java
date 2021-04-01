package Euler.java;

public class euler2 {
    static public void main(String[] args)
    {
        int x=1;
        int y=2;
        int ans=2;
        while (y<4000000)
        {
            int k=0;
            k=y;
            y=x+y;
            x=k;
            if (y%2==0)
            {
                ans+=y;
            }
        }
        System.out.println(ans);
    }
}
