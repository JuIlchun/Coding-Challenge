package Euler.java;

public class euler4 {
    public String revert(String name)
    {
        StringBuffer sb = new StringBuffer(name);
        String reversedStr=sb.reverse().toString();
        return reversedStr;
    }
    static public void main(String[] args)
    {
        euler4 euler = new euler4();
        String keep;
        int ans = 0;
        for (int i=317;i<1000;i++)
        {
            for (int j=317;j<1000;j++)
            {
                keep=Integer.toString(i*j);
                String front=keep.substring(0,3);
                keep=euler.revert(keep);
                String end=keep.substring(0,3);
                if (front.equals(end))
                {
                    if (i*j>ans)
                    {
                        ans=i*j;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
