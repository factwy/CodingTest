import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int[][] map = new int[n][n];
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++)
				map[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int[][][] prefix = new int[n+1][n+1][10];
		for(int i=0; i<=n; i++)
			for(int j=0; j<=n; j++) {
				for(int num=0; num<10; num++) {
					if(i == 0 || j == 0) {
						prefix[i][j][num] = 0;
						continue;
					}
					
					prefix[i][j][num] = prefix[i-1][j][num] + prefix[i][j-1][num] - prefix[i-1][j-1][num];
				}
				if(i != 0 && j != 0)
					prefix[i][j][map[i-1][j-1]-1] ++;
			}
		
		int q = Integer.parseInt(br.readLine());
		for(int a=0; a<q; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			
			int cnt = 0;
			for(int i=0; i<10; i++)
				if(prefix[x2][y2][i] - prefix[x1-1][y2][i] - prefix[x2][y1-1][i] + prefix[x1-1][y1-1][i] > 0)
					cnt ++;
			
			System.out.println(cnt);
		}
	}
}