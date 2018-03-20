import java.util.*;

public class Main 
{
	public static LinkedList<Integer> graph[];
	public static int t,n,k,w,indegree[],intime[],arr[][],result[];
	
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		t=sc.nextInt();
		
		for(int p=0;p<t;p++)
		{
			n=sc.nextInt();
			k=sc.nextInt();
			
			intime=new int[n];
			indegree=new int[n];
			
			graph=new LinkedList[n];
			arr=new int[n][n];
			result=new int[n];
			
			for(int i=0;i<n;i++)
			{
				graph[i]=new LinkedList<>();
			}
			
			for(int i=0;i<n;i++)
			{
				intime[i]=sc.nextInt();
			}
			
			for(int i=0;i<k;i++)
			{
				int from, to, m;
				
				from = sc.nextInt()-1;
				to =sc.nextInt()-1;
				
				graph[from].add(to);
				indegree[to]++;
			}
			w=sc.nextInt();
			
			topologicalSort();
			
			System.out.println(result[w-1]);
		}
	}
	
	public static void topologicalSort()
	{
		Queue<Integer> searchQ = new LinkedList<>();
		Queue<Integer> resultQ = new LinkedList<>();
		
		for(int i=0;i<n;i++)
		{
			if(indegree[i]==0)
			{
				searchQ.offer(i);
			}
		}
		
		result[0]=intime[0];
		
		while(!searchQ.isEmpty())
		{
			int zeroIndegreeNode = searchQ.poll();
			resultQ.offer(zeroIndegreeNode);
			
			for(int LinkedNode : graph[zeroIndegreeNode])
			{
				indegree[LinkedNode]--;
				
				arr[LinkedNode][zeroIndegreeNode]=intime[zeroIndegreeNode]+intime[LinkedNode];
				
				if(indegree[LinkedNode]==0)
				{
					searchQ.offer(LinkedNode);
					Arrays.sort(arr[LinkedNode]);
					result[LinkedNode]=arr[LinkedNode][n-1];
					intime[LinkedNode]=arr[LinkedNode][n-1];
				}
			}	
		}
	
	}
}

