import java.io.*;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] game = new int[101];
		for(int i=0; i<101; i++)
			game[i] = -1;
		game[1] = 0;
		
		Map<Integer, Integer> ladder = new HashMap<Integer, Integer>();
		Map<Integer, Integer> snake = new HashMap<Integer, Integer>();
		for(int i=0; i<n; i++) {
			StringTokenizer input = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(input.nextToken());
			int y = Integer.parseInt(input.nextToken());
			ladder.put(x, y);
		}
		for(int i=0; i<m; i++) {
			StringTokenizer input = new StringTokenizer(br.readLine(), " ");
			int u = Integer.parseInt(input.nextToken());
			int v = Integer.parseInt(input.nextToken());
			snake.put(u, v);
		}
		
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(1);
		while(q.isEmpty() == false) {
			int pos = q.poll();
			for(int i=6; i>0; i--) {
				int next_pos = pos + i;
				if(next_pos > 100) 
					continue;
				if(ladder.containsKey(next_pos))
					next_pos = ladder.get(next_pos);
				else if(snake.containsKey(next_pos))
					next_pos = snake.get(next_pos);
				
				if(game[next_pos] == -1 || game[pos] + 1 < game[next_pos]) {
					game[next_pos] = game[pos] + 1;
					q.offer(next_pos);
				}
			}
		}
		System.out.println(game[100]);
	}
}