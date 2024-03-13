import java.io.*;
import java.util.*;

public class Main {
	static int[][] islands, nation;
	static int n;
	static int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
	
	public static class Pos {
		int x, y, dist;
		Pos(int x, int y, int dist) {
			this.x = x;
			this.y = y;
			this.dist = dist;
		}
		Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		islands = new int[n][n];
		nation = new int[n][n];
		
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++) {
				islands[i][j] = Integer.parseInt(st.nextToken());
				nation[i][j] = 0;
			}
		}
		
		int nationCode = 1;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(islands[i][j] == 0 || nation[i][j] != 0)
					continue;
				
				boolean[][] visited = new boolean[n][n];
				visited[i][j] = true;
				Queue<Pos> q = new LinkedList<Pos>();
				q.offer(new Pos(i, j));
				nation[i][j] = nationCode;
				
				while(q.isEmpty() == false) {
					Pos nowPos = q.poll();
					int x = nowPos.x, y = nowPos.y;
					
					for(int index=0; index<4; index++) {
						int nx = x + dx[index], ny = y + dy[index];
						if(nx < 0 || nx >= n || ny < 0 || ny >= n)
							continue;
						if(visited[nx][ny] == true)
							continue;
							
						if(islands[nx][ny] == 1 && nation[nx][ny] != nationCode) {
							nation[nx][ny] = nationCode;
							q.offer(new Pos(nx, ny));
							visited[nx][ny] = true;
						}
					}
				}
				nationCode++;
			}
		}
		
		int min_dist = 200;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(islands[i][j] == 0)
					continue;
				int dist = bfs(i, j);
				if(dist == -1)
					continue;
				min_dist = (min_dist < dist) ? min_dist : dist;
			}
		}
		
		System.out.println(min_dist);
	}
	
	public static int bfs(int a, int b) {
		Queue<Pos> q = new LinkedList<Pos>();
		q.offer(new Pos(a, b, 0));
		
		boolean[][] visited = new boolean[n][n];
		visited[a][b] = true;
		
		while(q.isEmpty() == false) {
			Pos myPos = q.poll();
			int x = myPos.x, y = myPos.y, dist = myPos.dist;
			
			for(int i=0; i<4; i++) {
				int nx = x + dx[i], ny = y + dy[i];
				if(nx < 0 || nx >= n || ny < 0 || ny >= n)
					continue;
				
				if(visited[nx][ny] == true || nation[a][b] == nation[nx][ny])
					continue;
				if(islands[nx][ny] == 1)
					return dist;
				
				visited[nx][ny] = true;
				q.offer(new Pos(nx, ny, dist+1));
			}
		}
		return -1;
	}
}