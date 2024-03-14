import java.io.*;
import java.util.*;

public class Main {
	static int n, cnt;
	static int[][] map;
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		map = new int[n][n];
		for(int i=0; i<n; i++) {
			String input = br.readLine();
			for(int j=0; j<n; j++)
				map[i][j] = (input.charAt(j)) - '0';
		}
		
		visited = new boolean[n][n];
		ArrayList<Integer> town = new ArrayList();
		
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++) {
				if(visited[i][j] == true || map[i][j] == 0)
					continue;
				
				visited[i][j] = true;
				cnt = 0;
				dfs(i, j);
				town.add(cnt);
			}
		
		Collections.sort(town);
		System.out.println(town.size());
		for(int i=0; i<town.size(); i++)
			System.out.println(town.get(i));
	}
	
	public static void dfs(int x, int y) {
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		cnt++;
		
		for(int i=0; i<4; i++) {
			int nx = x + dx[i], ny = y + dy[i];
			if(nx < 0 || nx >= n || ny < 0 || ny >= n)
				continue;
			if(visited[nx][ny] == true || map[nx][ny] == 0)
				continue;
			visited[nx][ny] = true;
			dfs(nx, ny);
		}
	}
}