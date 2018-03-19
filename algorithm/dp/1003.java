import java.util.*;

public class Baekjoon 
{
	static fibo tmp[];
	static int result=0;
	static class fibo
	{
		int one;
		int zero;
		fibo plus(fibo a, fibo b)
		{
			fibo tmp=new fibo();;
			tmp.one=a.one+b.one;
			tmp.zero=a.zero+b.zero;
			return tmp;
		}
	}
	
	public static void fibonacci(int n)
	{
		if(tmp[n].one==0&&tmp[n].zero==0)
		{
			tmp[n]=tmp[n].plus(tmp[n-1],tmp[n-2]);			
		}
	}

	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int t=sc.nextInt();
		
		
		for(int i=0;i<t;i++)
		{
			int n=sc.nextInt();
			
			tmp=new fibo[n+1];
			for(int j=0;j<=n;j++)
				tmp[j]=new fibo();
			tmp[0].one=0;
			tmp[0].zero=1;
			if(n>=1)
			{
				tmp[1].one=1;
				tmp[1].zero=0;
			}
			for(int j=2;j<=n;j++)
				fibonacci(j);
			System.out.println(tmp[n].zero+" "+tmp[n].one);
		}
		
	}
}
