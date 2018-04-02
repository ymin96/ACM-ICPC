
import java.util.*;
import java.lang.*;
import java.math.*;
public class Main {

	public static void num1()
	{
		Scanner sc = new Scanner(System.in);
		
		while(true)
		{
			System.out.print("�Է�>");
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
			System.out.print("�Է�>");
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
			System.out.println("���������� :"+num);
			num = 0;
		}
		System.out.println("�����մϴ�!");
	}
	
	public static void num3()
	{
		Scanner sc=new Scanner(System.in);
		int sum=0,num=1,count=0;
		while(true)
		{
			System.out.print("�Է�> ");
			int n=sc.nextInt();
			if(n > 0)
			{
				sum+=n;
				num*=n;
				count++;
			}
			else if(n==0)
			{
				System.out.println("�հ��: "+sum+" �����: "+num);
				System.out.print("���: "+sum/count+" ");
				if(sum/count >= 90)
					System.out.println("����� ����: A");
				else if(sum/count >= 80)
					System.out.println("����� ����: B");
				else
					System.out.println("����� ����: C");
			}
			else if(n==-1)
				break;
		}
		System.out.println("�����մϴ�.");
	}
	
	public static void num4()
	{
		Scanner sc=new Scanner(System.in);
		
		while(true)
		{
			System.out.print("�Է�> ");
			int n=sc.nextInt();
			int k = 1;
			if(n%2==0)
				System.out.println("¦���Դϴ� �ٽ� �Է��ϼ���.");
			else if(n < 0)
			{
				System.out.println("�����մϴ�.");
				break;
			}
			else
			{
				for(int i=0;i<=n/2;i++)
				{
					for(int j=0;j<n/2-i;j++)
						System.out.print("��");
					System.out.print("��");
					if(i > 0)
					{
						for (int j=0;j<k;j++)
							System.out.print("��");
						System.out.print("��");
						k+=2;
					}
					System.out.println();
				}
				k=n-4;
				for(int i=0;i<n/2;i++)
				{
					for(int j=0;j<i+1;j++)
						System.out.print("��");
					System.out.print("��");
					if(i<n/2-1)
					{
						for(int j=0;j<k;j++)
							System.out.print("��");
						System.out.print("��");
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
			System.out.print("�Է�> ");
			int n=sc.nextInt();
			if(n<0)
				break;
			else if(n<5)
				System.out.println("5���� ū���� �Է��ϼž� �մϴ�.");
			else
			{
				
				for(int i=1;i<=n;i++)
				{
					System.out.print(i+":");
					if(i==1)
					{
						for(int j=0;j<n;j++)
							System.out.print("��");
					}
					else if(i==n)
					{
						for(int j=1;j<i;j++)
							System.out.print(" ");
						System.out.print("��");
					}
					else
					{
						for(int j=1;j<i;j++)
							System.out.print(" ");
						System.out.print("��");
						for(int j=0;j<n-1-i;j++)
							System.out.print(" ");
						System.out.print("��");
					}
					System.out.println();
				}
			}
		}
		System.out.println("����");
	}
	
	public static void num6()
	{
		Scanner sc=new Scanner(System.in);
		while(true)
		{
			System.out.print("���� ����(x1,y1)�Է�> ");
			int x1=sc.nextInt();
			int y1=sc.nextInt();
			if(x1<0||y1<0)
				break;
			System.out.print("������ �Ʒ���(x2,y2)�Է�> ");
			int x2=sc.nextInt();
			int y2=sc.nextInt();
			int row=x2-x1;
			int col=y2-y1;
			if(row*col>=30)
				System.out.println("�� ���� �簢���� �Է��ϼ���!");
			else
			{
				System.out.println("���:");
				System.out.println("�簢���� ����: "+ (row*col));
				System.out.println("�簢���� ���̴� "+row+", "+col+", "+row+", "+col+"   �밢���� �Ÿ��� "+(int)Math.sqrt((row*row)+(col*col)));
			}
		}
		System.out.println("����");
	}
	
	public static void num7()
	{
		Scanner sc=new Scanner(System.in);
		while(true)
		{
			System.out.print("�Է�> ");
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
					System.out.println("���� "+c+"���� ȭ�� "+f+"���Դϴ�." );
				}
				else if(str.equals("f"))
				{
					f=db;
					c=(f-32)/1.8;
					System.out.println("ȭ�� "+f+"���� ���� "+c+"���Դϴ�." );
				}
				if(c >= 25)
					System.out.println("������~");
				else if(c >= 10)
					System.out.println("������ �����Դϴ�~");
				else if(c >= -10)
					System.out.println("�ҽ��� �����׿�!");
				else if(c >= -30)
					System.out.println("������ ����ϴ�! ���� �����ϼ���!");
				else 
					System.out.println("�ѱ� ��� �½��ϱ�?");
			}
			else
				System.out.println("�ٽ� �Է��ϼ���~");
		}
		System.out.println("�����մϴ�!");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		boolean end=true;
		while(end)
		{
			System.out.print("���� ���� 1~7������(0�Է½� ����)> ");
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
