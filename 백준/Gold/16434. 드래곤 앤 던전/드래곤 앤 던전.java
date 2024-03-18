import java.io.*;
import java.util.*;

public class Main {	
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());
		long atk = Integer.parseInt(st.nextToken());
		
		int[][] map = new int[n][3];
		for(int i=0; i<n; i++) {
			st  = new StringTokenizer(br.readLine(), " ");
			
			int t = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			
			map[i][0] = t;
			map[i][1] = a;
			map[i][2] = h;
		}
		
		long start = 0, end = 100000000000000000L;
		long res = end;
		while(start <= end) {
			long mid = (start + end) / 2;
			
			long curHp = mid;
			long myAtk = atk;
			
			for(int i=0; i<n; i++) {
				if(map[i][0] == 1) {
					curHp -= (((map[i][2] + myAtk - 1) / myAtk) - 1) * map[i][1];
					if(curHp <= 0)
						break;
				} else {
					myAtk += map[i][1];
					curHp = Math.min(mid, curHp + map[i][2]);
				}
			}
			
			if(curHp > 0) {
				end = mid - 1;
				res = Math.min(res, mid);
			}
			else
				start = mid + 1;
		}
		
		System.out.println(res);
	}
}