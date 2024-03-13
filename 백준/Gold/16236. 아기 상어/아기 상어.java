import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		int[][] space = new int[n][n];
		int[] shark = new int[2];
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<n; j++) {
				space[i][j] = Integer.parseInt(st.nextToken());
				if(space[i][j] == 9)
					shark = new int[] {i, j};
			}
		}
		
		int cnt = 0;
		int shark_size = 2, needToGrow = 2, cntEat = 0;
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		
		for(;;) {
			int[][] cnt_dist = new int[n][n];
			for(int i=0; i<n; i++)
				for(int j=0; j<n; j++)
					cnt_dist[i][j] = -1;
			cnt_dist[shark[0]][shark[1]] = 0;
			
			int[][] smallFish = new int[n*n][2];
			int index = 0;
			for(int i=0; i<n; i++)
				for(int j=0; j<n; j++) {
					if(space[i][j] != 0 && space[i][j] < shark_size)
						smallFish[index++] = new int[] {i, j};
				}
			
			Queue<int[]> q = new LinkedList<int[]>();
			q.offer(shark);
			
			while(q.isEmpty() == false) {
				int[] pos = q.poll();
				int x = pos[0], y = pos[1];
				
				for(int i=0; i<4; i++) {
					int nx = x + dx[i], ny = y + dy[i];
					if(nx < 0 || nx >= n || ny < 0 || ny >= n)
						continue;
					if(space[nx][ny] > shark_size)
						continue;
					if(cnt_dist[nx][ny] == -1 || cnt_dist[x][y] + 1 < cnt_dist[nx][ny]) {
						cnt_dist[nx][ny] = cnt_dist[x][y] + 1;
						q.offer(new int[] {nx, ny});
					}
				}
			}
			
			int min_dist = -1, x = 0, y = 0;
			for(int i=0; i<index; i++) {
				int now_dist = cnt_dist[smallFish[i][0]][smallFish[i][1]];
				if(now_dist == -1)
					continue;
				if(min_dist == -1 || now_dist < min_dist) {
					min_dist = now_dist;
					x = smallFish[i][0];
					y = smallFish[i][1];
				}
			}
			
			if(min_dist == -1) {
				System.out.println(cnt);
				break;
			}
			cntEat ++;
			cnt += min_dist;
			if(cntEat == needToGrow) {
				needToGrow++;
				cntEat = 0;
				shark_size++;
			}
			
			space[x][y] = 9;
			space[shark[0]][shark[1]] = 0;
			shark = new int[] {x, y};
		}
	}
}