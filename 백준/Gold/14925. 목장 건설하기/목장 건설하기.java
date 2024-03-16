import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[m][n];
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++)
				map[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int[][] prefix = new int[m+1][n+1];
		for(int i=0; i<=m; i++)			
			for(int j=0; j<=n; j++) {
				if(i==0 || j==0)
					prefix[i][j] = 0;
				else
					prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + map[i-1][j-1]; 
			}
		
		int s = 0, e = Math.min(n, m);
		while(s <= e) {
			int mid = (s + e) / 2;
			boolean canMake = false;
			
			for(int i=mid; i<=m; i++) {
				if(canMake)
					break;
				for(int j=mid; j<=n; j++)
					if(prefix[i][j] - prefix[i-mid][j] - prefix[i][j-mid] + prefix[i-mid][j-mid] == 0) {
						canMake = true;
						break;
					}
			}
			
			if(!canMake)
				e = mid - 1;
			else
				s = mid + 1;
		}		
		System.out.println((s + e) / 2);
	}
}