import java.io.*;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		int l = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[m];
		st = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<m; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		Arrays.sort(arr);
		
		int res = 0;
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			int start = 0, end = m;
			while(start <= end) {
				int mid = (start + end) / 2;
				
				if(Math.abs(x - arr[mid]) + y <= l)
					break;
				
				if(x < arr[mid])
					end = mid - 1;
				else
					start = mid + 1;
			}
			
			if(Math.abs(x - arr[(start + end) / 2]) + y <= l)
				res ++;
		}
		
		System.out.println(res);
		 
	}
}