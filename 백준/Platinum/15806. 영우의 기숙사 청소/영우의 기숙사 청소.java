import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int t = Integer.parseInt(st.nextToken());
				
		boolean[][][] needToClean = new boolean[2][n][n];
		
		Queue<Pos> q = new LinkedList<Pos>();
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()) - 1;
			int y = Integer.parseInt(st.nextToken()) - 1;
			
			q.offer(new Pos(x, y, 0));
		}
		
		int[] dx = {-2, -2, -1, -1, 1, 1, 2, 2}, dy = {-1, 1, -2, 2, -2, 2, -1, 1};
		
		for(int a=0; a<t; a++) {
			int size = q.size();
			for(int b=0; b<size; b++) {
				Pos mypos = q.poll();
				int x = mypos.x, y = mypos.y, day = mypos.day;
				
				for(int i=0; i<8; i++) {
					int nx = x + dx[i], ny = y + dy[i];
					int cnt = (day + 1) % 2;
					
					if(0 <= nx && nx < n && 0 <= ny && ny < n && needToClean[cnt][nx][ny] == false) {
						needToClean[cnt][nx][ny] = true;
						q.offer(new Pos(nx, ny, day+1));
					}
				}
			}
		}
		
		for(int i=0; i<k; i++) {
			st = new StringTokenizer(br.readLine());
			
			int x = Integer.parseInt(st.nextToken()) - 1;
			int y = Integer.parseInt(st.nextToken()) - 1;
			
			if(needToClean[t%2][x][y] == true) {
				System.out.println("YES");
				return;
			}
		}
		System.out.println("NO");
		
		br.close();
	}
	
	public static class Pos {
		int x, y, day;
		Pos(int x, int y, int day) {
			this.x = x;
			this.y = y;
			this.day = day;
		}
	}
}