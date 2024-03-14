import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br;
	static int n, m, k;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		
		int[][] castle = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<m; j++)
				castle[i][j] = Integer.parseInt(st.nextToken());
		}
		
		int maxKill = 0;
		for(int d1=0; d1<(m-2); d1++)
			for(int d2=(d1+1); d2<(m-1); d2++)
				for(int d3=(d2+1); d3<m; d3++) {
					int[][] newCastle = new int[n][m];
					for(int i=0; i<n; i++)
						for(int j=0; j<m; j++)
							newCastle[i][j] = castle[i][j];
					
					int kill = bfs(newCastle, new int[] {d1, d2, d3});
					maxKill = Math.max(kill, maxKill);
				}
		
		System.out.println(maxKill);
	}
	
	public static int bfs(int[][] newCastle, int[] dex) {
		int res = 0;
				
		int[] dx = {0, -1, 0}, dy = {-1, 0, 1};
		for(int round=0; round<n; round++) {
			int[][] enemy = new int[n*m][2];
			int cntEnemy = 0;
			
			for(int d : dex) {
				Queue<int[]> q = new LinkedList<int[]>();
				boolean[][] visited = new boolean[n][m];
				
				q.offer(new int[] {n, d});
				while(q != null && q.isEmpty() == false) {
					int[] pos = q.poll();
					int x = pos[0], y = pos[1];
					
					for(int index=0; index<3; index++) {
						int nx = x + dx[index], ny = y + dy[index];
						if(nx < 0 || nx >= n || ny < 0 || ny >= m)
							continue;
						if(Math.abs(n - nx) + Math.abs(d - ny) > k || visited[nx][ny] == true)
							continue;
						if(newCastle[nx][ny] == 1) {
							enemy[cntEnemy++] = new int[] {nx, ny};
							q = null;
							break;
						}
						visited[nx][ny] = true;
						q.offer(new int[] {nx, ny});
					}
				}
			}
			
			for(int i=0; i<cntEnemy; i++) {
				int x = enemy[i][0], y = enemy[i][1];
				if(newCastle[x][y] == 1) {
					res++;
					newCastle[x][y] = 0;
				}
			}
			
			for(int i=n-2; i>=0; i--) 
				for(int j=0; j<m; j++) 
					newCastle[i+1][j] = newCastle[i][j];
			
			for(int i=0; i<m; i++)
				newCastle[0][i] = 0;
		}
		
		return res;
	}
}