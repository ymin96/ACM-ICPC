import java.util.*;


class Elements
{
	int x,y,divNum;
	public Elements(int x, int y, int divNum)
	{
		this.x=x;
		this.y=y;
		this.divNum=divNum;
	}
}

public class Main 
{
	static int row_data[][]=new int[9][10];
	static int col_data[][]=new int[9][10];
	static int sec_data[][]=new int[9][10];
	static int arr[][]=new int[9][9];
	static ArrayList<Elements> zero_arr=new ArrayList<Elements>();
	
	public static void check()
	{
		for(int i=0;i<9;i++)
		{
			for(int j=0;j<9;j++)
			{
				row_data[i][arr[i][j]] = 1;
				col_data[j][arr[i][j]] = 1;
				sec_data[(i/3)*3+j/3][arr[i][j]]=1;
			}
		}
	}
	
	public static void DFS(int num)
	{
		if(num>=zero_arr.size())
			return;
		
		Elements tmp=zero_arr.get(num);

		for(int i=1;i<10;i++)
		{
			if(row_data[tmp.y][i]==0&&col_data[tmp.x][i]==0&&sec_data[tmp.divNum][i]==0)
			{
				arr[tmp.y][tmp.x]=i;
				row_data[tmp.y][i]=1;
				col_data[tmp.x][i]=1;
				sec_data[tmp.divNum][i]=1;
				DFS(num+1);
				if(end_check()==0)
					return;
				arr[tmp.y][tmp.x]=0;
				row_data[tmp.y][i]=0;
				col_data[tmp.x][i]=0;
				sec_data[tmp.divNum][i]=0;
			}
		}
	}
	
	public static int end_check()
	{
		int count=0;
		for(int i=0;i<9;i++)
		{
			for(int j=0;j<9;j++)
			{
				if(arr[i][j]==0)
				{
					count++;
				}
			}
		}
		if(count==0)
			return 0;
		else
			return 1;
	}
	
	public static void print()
	{
		for(int i=0;i<9;i++)
		{
			for(int j=0;j<9;j++)
			{
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		for(int i=0;i<9;i++)
		{
			for(int j=0;j<9;j++)
			{
				arr[i][j]=sc.nextInt();
				if(arr[i][j]==0)
				{
					int div=(i/3)*3+j/3;
					zero_arr.add(new Elements(j,i,div));
				}
			}
		}
		
		check();
		DFS(0);
		print();
	}
}
