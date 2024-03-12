import java.io.*;
import java.util.*;

public class Main {	
	static int l, w;
	static char[][] map;
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer map_size = new StringTokenizer(br.readLine(), " ");
		
		l = Integer.parseInt(map_size.nextToken());
		w = Integer.parseInt(map_size.nextToken());
		
		map = new char[l][w];
		for(int i=0; i<l; i++) {
			String now_map = br.readLine();
			for(int j=0; j<w; j++)
				map[i][j] = now_map.charAt(j);
		}
		
		int time = 0;
		for(int i=0; i<l; i++) {
			for(int j=0; j<w; j++) {
				if(map[i][j] == 'W')
					continue;
				int now_time = bfs(i, j);
				time = (time > now_time) ? time : now_time;
			}
		}
		
		System.out.println(time);
	}
	
	public static int bfs(int i, int j) {
		Queue<int[]> q = new LinkedList();
        
		boolean[][] visited = new boolean[l][w];
		visited[i][j] = true;
		q.offer(new int[] {i, j, 0});
        
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		int max_dis = 0;
		
		while(q.isEmpty() == false) {
			int[] pos = q.poll();
			int x = pos[0], y = pos[1], dis = pos[2];
			max_dis = (max_dis > dis) ? max_dis : dis;
			
			for(int index=0; index<4; index++) {
				int nx = x + dx[index], ny = y + dy[index];
				if(nx < 0 || nx >= l || ny < 0 || ny >= w)
					continue;
				if(map[nx][ny] == 'W' || visited[nx][ny] == true)
					continue;
				visited[nx][ny] = true;
				q.offer(new int[] {nx, ny, dis+1});
			}
		}
		return max_dis;
	}
}