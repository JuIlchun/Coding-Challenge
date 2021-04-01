package Euler.java;

public class euler5 {
    public static void main(String[] args)
    {
        int end=0;
        int num=1;
        while (end<20)
        {
            end=0;
            for (int i=1;i<21;i++)
            {
                if (num%i==0)
                {
                    end++;
                }
                if (i!=end) break;
            }
            num++;
        }
        System.out.printf("%d %d \n", num-1, end);
    }
}
