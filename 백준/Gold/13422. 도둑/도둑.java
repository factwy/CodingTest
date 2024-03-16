import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		
		for(; t>0; t--) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			
			int[] house = new int[n+(m-1)];
			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<n; i++)
				house[i] = Integer.parseInt(st.nextToken());
			for(int i=0; i<(m-1); i++)
				house[n+i] = house[i];
						
			int[] prefix = new int[n+m];
			prefix[0] = 0;
			for(int i=1; i<(n+m); i++)
				prefix[i] = prefix[i-1] + house[i-1];
			
			int cnt = 0;
			if(n != m) {
				for(int i=0; i<n; i++)
					if(prefix[i+m] - prefix[i] < k)
						cnt++;
			} else
				if(prefix[n] - prefix[0] < k)
					cnt++;
			
			System.out.println(cnt);
		}
	}
}