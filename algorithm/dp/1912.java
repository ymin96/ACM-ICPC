import java.util.*;

public class Main {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int arr[] = new int[n];
		for (int i = 0; i < n; i++)
			arr[i] = sc.nextInt();

		int max = arr[0], temp = arr[0];

		for (int i = 0; i < arr.length; i++) {
			if (temp < arr[i])
				temp = arr[i];
		}
		if (temp <= 0) {
			System.out.println(temp);
		} else {
			int i;
			for(i=0;i<arr.length;i++) {
				if(arr[i]>0)
					break;
			}
			max=arr[i];
			temp=arr[i];
			for (i =i + 1; i < arr.length; i++) {
				temp += arr[i];
				if (temp > max)
					max = temp;
				if(temp<0) {
					int j;
					for(j=i;j<arr.length;j++) {
						if(arr[j]>0)
							break;
					}
					temp=0;
					i=j-1;
				}
			}
			System.out.println(max);
		}
	}
}