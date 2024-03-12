import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer box_size = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(box_size.nextToken());
		int n = Integer.parseInt(box_size.nextToken());
		
		int[][] box = new int[n][m];
		int[][] tomatos = new int[n*m][2];
		int init_tomato = 0;
		
		for(int i=0; i<n; i++) {
			StringTokenizer now_box = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				box[i][j] = Integer.parseInt(now_box.nextToken());
				if(box[i][j] == 1)
					tomatos[init_tomato++] = new int[] {i, j};
			}
		}
		
		Queue<int[]> q = new LinkedList();
		for(int i=0; i<init_tomato; i++)
			q.offer(tomatos[i]);
		
		int[] dx = new int[]{-1, 0, 1, 0};
		int[] dy = new int[]{0, -1, 0, 1};
		
		while(q.isEmpty() != true) {
			int[] pos = q.poll();
			int x = pos[0], y = pos[1];
			
			for(int i=0; i<4; i++) {
				int nx = x + dx[i], ny = y + dy[i];
				if(nx < 0 || nx >= n || ny < 0 || ny >= m)
					continue;
				if(box[nx][ny] != 0)
					continue;
				
				box[nx][ny] = box[x][y] + 1;
				q.offer(new int[] {nx, ny});
			}
		}
		
		int res = 0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(box[i][j] == 0) {
					System.out.println("-1");
					return;
				}
				res = (res > box[i][j]) ? res : box[i][j];
			}
		}
		System.out.println(res-1);
	}
}
