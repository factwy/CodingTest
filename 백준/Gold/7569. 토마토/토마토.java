import java.io.*;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer box_size = new StringTokenizer(br.readLine(), " ");
		
		int m = Integer.parseInt(box_size.nextToken());
		int n = Integer.parseInt(box_size.nextToken());
		int h = Integer.parseInt(box_size.nextToken());
		
		int[][][] box = new int[h][n][m];
		int[][] tomatos = new int[h*n*m][3];
		int init_tomato = 0;
		
		for(int x=0; x<h; x++)
			for(int y=0; y<n; y++) {
				StringTokenizer now_box = new StringTokenizer(br.readLine(), " ");
				for(int z=0; z<m; z++) {
					box[x][y][z] = Integer.parseInt(now_box.nextToken());
					if(box[x][y][z] == 1) {
						tomatos[init_tomato++] = new int[]{x, y, z};
					}
				}
			}
		
		int[] dx = {-1, 0, 1, 0, 0, 0};
		int[] dy = {0, -1, 0, 1, 0, 0};
		int[] dz = {0, 0, 0, 0, -1, 1};
		
		Queue<int[]> q = new LinkedList();
		for(int i=0; i<init_tomato; i++)
			q.add(tomatos[i]);
		
		while(q.isEmpty() == false) {
			int[] pos = q.poll();
			int x = pos[0], y = pos[1], z = pos[2];
			
			for(int i=0; i<6; i++) {
				int nx = x + dx[i], ny = y + dy[i], nz = z + dz[i];
				if(nx < 0 || nx >= h || ny <0 || ny >= n || nz < 0 || nz >= m)
					continue;
				if(box[nx][ny][nz] != 0)
					continue;
				box[nx][ny][nz] = box[x][y][z] + 1;
				q.add(new int[] {nx, ny, nz});
			}
		}
		
		int res = 0;
		for(int x=0; x<h; x++)
			for(int y=0; y<n; y++)
				for(int z=0; z<m; z++) {
					if(box[x][y][z] == 0) {
						System.out.println(-1);
						return;
					}
					res = (res > box[x][y][z]) ? res : box[x][y][z];
				}
		
		System.out.println(res-1);
	}
}