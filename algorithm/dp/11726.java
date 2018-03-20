import java.lang.reflect.Array;
import java.util.*;
import java.math.*;

public class Main 
{
	static long dp[]=new long[1001];
	
	public static long fibo(int n)
	{
		if(dp[n] != 0)
			return dp[n];
		if(n == 1)
			return 1;
		if(n == 2)
			return 2;
		
		long result = fibo(n-1)+fibo(n-2);
		
		dp[n]=result%10007;
		
		return result%10007;
		
	}
	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		
		dp[1]=1;
		dp[2]=2;
		System.out.println(fibo(n));
	}

}
