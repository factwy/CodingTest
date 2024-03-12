import java.io.*;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
	
		if(n == 1) {
			br.read();
			System.out.print("1 1");
			return ;
		}
				
		char[][] gridColor = new char[n][n];
		char[][] gridNotColor = new char[n][n];
		for(int i=0; i<n; i++) {
			String color = br.readLine();
			for(int j=0; j<n; j++) {
				char now_color = color.charAt(j);
				gridColor[i][j] = now_color;
				if(now_color == 'R')
					now_color = 'G';
				gridNotColor[i][j] = now_color;
			}
		}
		int cntColor = 0, cntNotColor = 0;
		int[] dx = {-1, 0, 1, 0}, dy = {0, -1, 0, 1};
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				// Color
				if(gridColor[i][j] != 'P') {
					Queue<int[]> q = new LinkedList();
					q.offer(new int[] {i, j});
					char init_color = gridColor[i][j];
					gridColor[i][j] = 'P';
					
					while(q.isEmpty() == false) {
						int[] pos = q.poll();
						int x = pos[0], y = pos[1];
						for(int index=0; index<4; index++) {
							int nx = x + dx[index], ny = y + dy[index];
							if(nx <0 || nx >= n || ny < 0 || ny >= n)
								continue;
							if(init_color != gridColor[nx][ny])
								continue;
							
							gridColor[nx][ny] = 'P';
							q.offer(new int[] {nx, ny});
						}
					}
					cntColor ++;
				}				
				
				// NotColor
				if(gridNotColor[i][j] != 'P') {
					Queue<int[]> q = new LinkedList();
					q.offer(new int[] {i, j});
					char init_color = gridNotColor[i][j];
					gridNotColor[i][j] = 'P';
					
					while(q.isEmpty() == false) {
						int[] pos = q.poll();
						int x = pos[0], y = pos[1];
						for(int index=0; index<4; index++) {
							int nx = x + dx[index], ny = y + dy[index];
							if(nx <0 || nx >= n || ny < 0 || ny >= n)
								continue;
							if(init_color != gridNotColor[nx][ny])
								continue;
							
							gridNotColor[nx][ny] = 'P';
							q.offer(new int[] {nx, ny});
						}
					}
					cntNotColor ++;
				}
			}
		}
		System.out.printf("%d %d", cntColor, cntNotColor);
	}
}