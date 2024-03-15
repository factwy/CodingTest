import java.io.*;
import java.util.*;

class Pos {
	int x, y;
	Pos(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Main {
	static int r, c;
	static int[][] map;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		map = new int[r][c];
		Pos[] target = new Pos[2];
		int index = 0;
		Queue<Pos> q = new LinkedList<Pos>();
		
		for(int i=0; i<r; i++) {
			String input = br.readLine();
			for(int j=0; j<c; j++) {
				char a = input.charAt(j);
				switch(a) {
				case 'X': {
					map[i][j] = 3000;
					break;
				}
				case 'L':
					target[index++] = new Pos(i, j);
				case '.':
					map[i][j] = 0;
					q.offer(new Pos(i, j));
				}
			}
		}
		
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		
		while(q.isEmpty() == false) {
			Pos pos = q.poll();
			
			for(int i=0; i<4; i++) {
				int nx = pos.x + dx[i], ny = pos.y + dy[i];
				
				if(nx < 0 || nx >= r || ny < 0 || ny >= c)
					continue;
				if(map[pos.x][pos.y] +1 < map[nx][ny]) {
					map[nx][ny] = map[pos.x][pos.y] + 1;
					q.offer(new Pos(nx, ny));
				}
			}
		}
		
		int res = binary_search(0, 1500, target[0], target[1]);
		System.out.println(res);
	}
	
	public static int binary_search(int s, int e, Pos t1, Pos t2) {
		int mid = (s+e) / 2;
		
		while(s < e) {
			mid = (s + e) / 2;
					
			Queue<Pos> q = new LinkedList<Pos>();
			int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
			boolean[][] visited = new boolean[r][c];
					
			q.offer(t1);
			visited[t1.x][t1.y] = true;
			
			while(q.isEmpty() == false) {
				Pos pos = q.poll();
				
				for(int i=0; i<4; i++) {
					int nx = pos.x + dx[i], ny = pos.y + dy[i];
					if(nx < 0 || nx >= r || ny < 0 || ny >= c)
						continue;
					if(map[nx][ny] > mid || visited[nx][ny] == true)
						continue;
					
					visited[nx][ny] = true;
					q.offer(new Pos(nx, ny));
				}
			}
			
			if(visited[t2.x][t2.y])
				e = mid;
			else
				s = mid + 1;
		}
		return (s+e) / 2;
	}
}