import java.util.*;

public class Main 
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		
		int arr[][]=new int[n][n];
		int t=sc.nextInt();
		
		for(int i=0;i<t;i++)
		{
			int x=sc.nextInt()-1;
			int y=sc.nextInt()-1;
			arr[x][y]=1;
			arr[y][x]=1;
		}
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(i==j)
					arr[i][j]=0;
				else if(arr[i][j]==0)
					arr[i][j]=1000;
			}
		}
		
		for(int k=0;k<n;k++)
		{
			for(int i=0;i<n;i++)
			{
				for(int j=0;j<n;j++)
				{
					arr[i][j]=(arr[i][j]>arr[i][k]+arr[j][k]) ? (arr[i][k]+arr[j][k]) : (arr[i][j]);
					arr[j][i]=(arr[j][i]>arr[k][i]+arr[k][j]) ? (arr[k][i]+arr[k][j]) : (arr[j][i]);
				}
			}
		}
		
		int count=0;
		for(int i=0;i<n;i++)
		{
			if(arr[0][i]<1000)
				count++;
		}
		System.out.println(count-1);
	}
}

