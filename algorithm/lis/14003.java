import java.lang.reflect.Array;
import java.util.*;
import java.math.*;

public class Main 
{
	static Vector<Integer> vector=new Vector<Integer>();
	static int arr[]=new int[1000000];
	static int first[];
	static int second[];
	static Stack<Integer> stk = new Stack<Integer>();
	public static int binary(int key, int low, int high)
	{
		int middle;
		middle=(low+high)/2;
		if(low<=high)
		{
			if(key==vector.elementAt(middle))
				return middle;
			else if(key<vector.elementAt(middle))
				return binary(key,low,middle-1);
			else
				return binary(key,middle+1,high);
		}
		if(low>high)
			return low;
		else
			return high;
	}
	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int lis = 0;
		
		first=new int[n];
		second=new int[n];
		
		for(int i=0;i<n;i++)
			arr[i]=sc.nextInt();
		
		vector.addElement(arr[0]);
		first[0]=0;
		second[0]=arr[0];
		lis=0;
		int max=0;
		for(int i=1;i<n;i++)
		{
			if(arr[i]>vector.elementAt(lis))
			{
				vector.addElement(arr[i]);				
				lis++;
				first[i]=lis;
				second[i]=arr[i];
			}
			else
			{
				int tmp=binary(arr[i],0,lis);
				vector.remove(tmp);
				vector.add(tmp,arr[i]);
				first[i]=tmp;
				second[i]=arr[i];
			}
		}
		
		System.out.println(lis+1);
		
		max=lis;
		for(int i=n-1;i>=0;i--)
		{
			if(first[i] == max)
			{
				stk.push(second[i]);
				max--;
			}
		}
		for(int i=0;i<lis+1;i++)
			System.out.print(stk.pop()+" ");
	}
}
