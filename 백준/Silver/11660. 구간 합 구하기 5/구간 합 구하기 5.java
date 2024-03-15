import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[n][n];
		int[][] prefix = new int[n+1][n+1];
		
		for(int i=0; i<n+1; i++) {
			if(i != 0)
				st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n+1; j++) {
				if(i == 0 || j == 0)
					prefix[i][j] = 0;
				else {
					map[i-1][j-1] = Integer.parseInt(st.nextToken());
					prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + map[i-1][j-1];
				}
			}
		}
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			int sum = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1];
			System.out.println(sum);
		}
	}
}