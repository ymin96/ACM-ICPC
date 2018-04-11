import java.util.*;

public class Main {
	
	static int n,m,k;
	public static void DFS(int arr[][],int x,int y) {
		arr[y][x]=2;
		if(y>0&&arr[y-1][x]==1)
			DFS(arr,x,y-1);
		if(y<n-1&&arr[y+1][x]==1)
			DFS(arr,x,y+1);
		if(x>0&&arr[y][x-1]==1)
			DFS(arr,x-1,y);
		if(x<m-1&&arr[y][x+1]==1)
			DFS(arr,x+1,y);
	}
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int t=sc.nextInt();
		
		for(int h=0;h<t;h++) {
			m=sc.nextInt();
			n=sc.nextInt();
			k=sc.nextInt();
			int count=0;
			int[][] arr=new int[n][m];
			
			for(int i=0;i<k;i++) {
				int x=sc.nextInt();
				int y=sc.nextInt();
				arr[y][x]=1;
			}
			
			for(int i=0;i<n;i++) {
				for(int j=0;j<m;j++) {
					if(arr[i][j]==1) {
						DFS(arr,j,i);
						count++;
					}
				}
			}
			
			System.out.println(count);
		}
	}
}