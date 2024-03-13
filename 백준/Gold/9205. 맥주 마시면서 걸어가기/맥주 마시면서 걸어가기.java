import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br;
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		while(t-- > 0) {
			festival();
		}
	}
	
	public static void festival() throws IOException{
		int n = Integer.parseInt(br.readLine());
		int[][] loc = new int[n+2][2];
		for(int i=0; i<n+2; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			loc[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
		}
		
		Queue<int[]> q = new LinkedList<int[]>();
		boolean[] move = new boolean[n+2];
		move[0] = true;
		q.offer(new int[] {loc[0][0], loc[0][1], 0});
		
		while(q.isEmpty() == false) {
			int[] pos = q.poll();
			int x = pos[0], y = pos[1], now = pos[2];
			if(x == loc[n+1][0] && y == loc[n+1][1])
				break;
			for(int i=1; i<n+2; i++) {
				int nx = loc[i][0], ny = loc[i][1];
				
				if(now == i || move[i] == true)
					continue;
				if(Math.abs(x - nx) + Math.abs(y - ny) <= 1000) {
					move[i] = true;
					q.offer(new int[] {nx, ny, i});
				}
			}
		}
		
		if(move[n+1] == true)
			System.out.println("happy");
		else
			System.out.println("sad");
		
	}
}