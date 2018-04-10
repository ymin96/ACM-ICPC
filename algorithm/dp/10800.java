import java.util.*;

public class Main {

	public static class Color_ball {
		int num;
		int color;
		long size;
		long value;
	}

	public static void q_sort(Color_ball m_arr[], int left, int right) {
		if (left < right) {
			int q = partition(m_arr, left, right);
			q_sort(m_arr, left, q - 1);
			q_sort(m_arr, q + 1, right);
		}
	}

	public static void swap(Color_ball m_arr[], int left, int right) {
		Color_ball temp;
		temp = m_arr[left];
		m_arr[left] = m_arr[right];
		m_arr[right] = temp;
	}

	public static int partition(Color_ball m_arr[], int left, int right) {
		long pivot;
		int low, high;
		low = left;
		high = right + 1;
		pivot = m_arr[left].size;
		do {
			do
				low++;
			while (low <= right && m_arr[low].size < pivot);
			do
				high--;
			while (high >= left && m_arr[high].size > pivot);
			if (low < high)
				swap(m_arr, low, high);
		} while (low < high);
		swap(m_arr, left, high);
		return high;
	}

	public static void solve(Color_ball m_arr[], int t_arr[], int n, ArrayList list[],int color_count[]) {
		long sum_value=0;
		list[m_arr[0].color].add(m_arr[0].size);
		color_count[m_arr[0].color]++;
		for (int i = 1; i < n; i++) {
			sum_value+=m_arr[i - 1].size;
			if(m_arr[i].size==m_arr[i-1].size)
				m_arr[i].value=m_arr[i-1].value;
			else
				m_arr[i].value = sum_value;
			list[m_arr[i].color].add(m_arr[i].size);
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < list[m_arr[i].color].size(); j++) {
				if((long)list[m_arr[i].color].get(j)<m_arr[i].size)
					m_arr[i].value -= (long) list[m_arr[i].color].get(j);
				else
					break;
			}
			t_arr[m_arr[i].num] = (int) m_arr[i].value;
		}
	}

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int t_arr[] = new int[n];
		Color_ball m_arr[] = new Color_ball[n];
		ArrayList<Long> list[] = new ArrayList[200001];
		int color_count[]=new int[200001];

		for (int i = 0; i < 200001; i++) {
			list[i] = new ArrayList<Long>();
			color_count[i]=0;
		}
		for (int i = 0; i < n; i++) {
			m_arr[i] = new Color_ball();
			m_arr[i].color = sc.nextInt();
			m_arr[i].size = sc.nextLong();
			m_arr[i].num = i;
			m_arr[i].value = 0;
			t_arr[i] = 0;
		}

		q_sort(m_arr, 0, n - 1);
		solve(m_arr, t_arr, n, list, color_count);
		
		for (int i = 0; i < n; i++)
			System.out.println(t_arr[i]);
	}
}