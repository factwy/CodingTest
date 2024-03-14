import java.io.*;
import java.util.*;

public class Main {
	static int n;
	static int[][] map;
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		map = new int[n][n];
		for(int i=0; i<n; i++) {
			StringTokenizer st  = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++)
				map[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int maxCnt = 0;
		
		for(int h=0; h<=100; h++) {
			visited = new boolean[n][n];
			int cnt = 0;
			for(int i=0; i<n; i++)
				for(int j=0; j<n; j++) {
					if(visited[i][j] == true)
						continue;
					
					if(map[i][j] > h) {
						visited[i][j] = true;
						dfs(i, j, h);
						cnt ++;
					}
				}
			maxCnt = Math.max(maxCnt, cnt);
		}
		
		System.out.println(maxCnt);
	}
	
	public static void dfs(int x, int y, int h) {
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			if(nx < 0 || nx >= n || ny < 0 || ny >= n)
				continue;
			
			if(visited[nx][ny] == true || map[nx][ny] <= h)
				continue;
			
			visited[nx][ny] = true;
			dfs(nx, ny, h);
		}
	}
	
}