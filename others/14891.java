
import java.util.*;
import java.lang.*;
import java.math.*;
public class Main {

	public static void num1()
	{
		Scanner sc = new Scanner(System.in);
		
		while(true)
		{
			System.out.print("입력>");
			int a=sc.nextInt();
			if(a < 0)
				break;
			int b=sc.nextInt();
			for(int i=1;i <= b ;i++)
			{
				System.out.print(i+":");
				for(int j=1;j<i;j++)
					System.out.print(" ");
				for(int j=0;j<i;j++)
					System.out.print("Hello World! ");
				for(int j=0;j<a;j++)
					System.out.println();
			}
		}
	}

	public static void num2()
	{
		Scanner sc=new Scanner(System.in);
		int num=0;
		while(true)
		{
			System.out.print("입력>");
			int a=sc.nextInt();
			int b=sc.nextInt();
			if(a==0&&b==0)
				break;
			for (int i=1;i<=b;i++)
			{
				num=a;
				System.out.print(i+": ");
				for(int j=0;j<i;j++)
				{
					if(j==i-1)
						System.out.print(a+" ");
					else
					{
						System.out.print(a+" x ");
						num*=a;
					}
				}
				System.out.println("= "+num);				
			}
			System.out.println("최종연산결과 :"+num);
			num = 0;
		}
		System.out.println("종료합니다!");
	}
	
	public static void num3()
	{
		Scanner sc=new Scanner(System.in);
		int sum=0,num=1,count=0;
		while(true)
		{
			System.out.print("입력> ");
			int n=sc.nextInt();
			if(n > 0)
			{
				sum+=n;
				num*=n;
				count++;
			}
			else if(n==0)
			{
				System.out.println("합결과: "+sum+" 곱결과: "+num);
				System.out.print("평균: "+sum/count+" ");
				if(sum/count >= 90)
					System.out.println("평균의 학점: A");
				else if(sum/count >= 80)
					System.out.println("평균의 학점: B");
				else
					System.out.println("평균의 학점: C");
			}
			else if(n==-1)
				break;
		}
		System.out.println("종료합니다.");
	}
	
	public static void num4()
	{
		Scanner sc=new Scanner(System.in);
		
		while(true)
		{
			System.out.print("입력> ");
			int n=sc.nextInt();
			int k = 1;
			if(n%2==0)
				System.out.println("짝수입니다 다시 입력하세요.");
			else if(n < 0)
			{
				System.out.println("종료합니다.");
				break;
			}
			else
			{
				for(int i=0;i<=n/2;i++)
				{
					for(int j=0;j<n/2-i;j++)
						System.out.print("　");
					System.out.print("■");
					if(i > 0)
					{
						for (int j=0;j<k;j++)
							System.out.print("　");
						System.out.print("■");
						k+=2;
					}
					System.out.println();
				}
				k=n-4;
				for(int i=0;i<n/2;i++)
				{
					for(int j=0;j<i+1;j++)
						System.out.print("　");
					System.out.print("■");
					if(i<n/2-1)
					{
						for(int j=0;j<k;j++)
							System.out.print("　");
						System.out.print("■");
						k-=2;
					}
					System.out.println();
				}
			}
		}
	}

	public static void num5()
	{
		Scanner sc=new Scanner(System.in);
		while(true)
		{
			System.out.print("입력> ");
			int n=sc.nextInt();
			if(n<0)
				break;
			else if(n<5)
				System.out.println("5보다 큰값을 입력하셔야 합니다.");
			else
			{
				
				for(int i=1;i<=n;i++)
				{
					System.out.print(i+":");
					if(i==1)
					{
						for(int j=0;j<n;j++)
							System.out.print("□");
					}
					else if(i==n)
					{
						for(int j=1;j<i;j++)
							System.out.print(" ");
						System.out.print("□");
					}
					else
					{
						for(int j=1;j<i;j++)
							System.out.print(" ");
						System.out.print("□");
						for(int j=0;j<n-1-i;j++)
							System.out.print(" ");
						System.out.print("□");
					}
					System.out.println();
				}
			}
		}
		System.out.println("종료");
	}
	
	public static void num6()
	{
		Scanner sc=new Scanner(System.in);
		while(true)
		{
			System.out.print("왼쪽 윗점(x1,y1)입력> ");
			int x1=sc.nextInt();
			int y1=sc.nextInt();
			if(x1<0||y1<0)
				break;
			System.out.print("오른쪽 아랫점(x2,y2)입력> ");
			int x2=sc.nextInt();
			int y2=sc.nextInt();
			int row=x2-x1;
			int col=y2-y1;
			if(row*col>=30)
				System.out.println("더 작은 사각형을 입력하세요!");
			else
			{
				System.out.println("출력:");
				System.out.println("사각형의 넓이: "+ (row*col));
				System.out.println("사각형의 길이는 "+row+", "+col+", "+row+", "+col+"   대각선의 거리는 "+(int)Math.sqrt((row*row)+(col*col)));
			}
		}
		System.out.println("종료");
	}
	
	public static void num7()
	{
		Scanner sc=new Scanner(System.in);
		while(true)
		{
			System.out.print("입력> ");
			String str=new String();
			str=sc.next();
			double db=sc.nextDouble();
			double c=0,f=0;
			if(str.equals("x"))
				break;
			else if(str.equals("c")||str.equals("f"))
			{
				if(str.equals("c"))
				{
					c=db;
					f=(c*1.8)+32;
					System.out.println("섭씨 "+c+"도는 화씨 "+f+"도입니다." );
				}
				else if(str.equals("f"))
				{
					f=db;
					c=(f-32)/1.8;
					System.out.println("화씨 "+f+"도는 섭씨 "+c+"도입니다." );
				}
				if(c >= 25)
					System.out.println("더워요~");
				else if(c >= 10)
					System.out.println("쾌적한 날씨입니다~");
				else if(c >= -10)
					System.out.println("쌀쌀한 날씨네요!");
				else if(c >= -30)
					System.out.println("날씨가 춥습니다! 외출 자제하세요!");
				else 
					System.out.println("한국 기온 맞습니까?");
			}
			else
				System.out.println("다시 입력하세요~");
		}
		System.out.println("종료합니다!");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		boolean end=true;
		while(end)
		{
			System.out.print("문제 선택 1~7번까지(0입력시 종료)> ");
			int n=sc.nextInt();
			
			switch(n)
			{
			case 1:
				num1();
				break;
			case 2:
				num2();
				break;
			case 3:
				num3();
				break;
			case 4:
				num4();
				break;
			case 5:
				num5();
				break;
			case 6:
				num6();
				break;
			case 7:
				num7();
				break;
			case 0:
				end=false;
				break;
			}
		}
	}

}
