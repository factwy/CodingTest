import java.io.*;
import java.util.*;

public class Main {
	static int m, n, cnt;
	static int[][] map;
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		map = new int[m][n];
		for(int i=0; i<m; i++)
			for(int j=0; j<n; j++)
				map[i][j] = 0;
		
		while(k-- > 0) {
			st = new StringTokenizer(br.readLine(), " ");
			int y1 = Integer.parseInt(st.nextToken());
			int x1 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken()) - 1;
			int x2 = Integer.parseInt(st.nextToken()) - 1;
			
			for(int i=x1; i<=x2; i++)
				for(int j=y1; j<=y2; j++)
					map[i][j] = 1;
		}
		
		ArrayList<Integer> arr = new ArrayList();
		visited = new boolean[n][n];
		
		for(int i=0; i<m; i++)
			for(int j=0; j<n; j++) {
				if(visited[i][j] == false && map[i][j] == 0) {
					visited[i][j] = true;
					cnt = 1;
					dfs(i, j);
					arr.add(cnt);
				}
			}
		
		Collections.sort(arr);
		System.out.println(arr.size());
		for(int a : arr)
			System.out.printf("%d ", a);
	}
	
	public static void dfs(int x, int y) {
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			if(nx < 0 || nx >= m || ny < 0 || ny >= n)
				continue;
			if(visited[nx][ny] == true || map[nx][ny] == 1)
				continue;
			
			visited[nx][ny] = true;
			cnt++;
			dfs(nx, ny);
		}
	}
	
}