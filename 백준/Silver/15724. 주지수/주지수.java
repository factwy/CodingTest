import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		
		int[][] prefix = new int[r+1][c+1];
		for(int i=0; i<r+1; i++) {
			if(i != 0)
				st = new StringTokenizer(br.readLine());
			for(int j=0; j<c+1; j++) {
				if(i==0 || j==0)
					prefix[i][j] = 0;
				else {
					int num = Integer.parseInt(st.nextToken());
					prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + num;
				}
			}
		}
		
		int q = Integer.parseInt(br.readLine());
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=0; i<q; i++) {
			st = new StringTokenizer(br.readLine());
			int r1 = Integer.parseInt(st.nextToken());
			int c1 = Integer.parseInt(st.nextToken());
			int r2 = Integer.parseInt(st.nextToken());
			int c2 = Integer.parseInt(st.nextToken());
			
			int sum = prefix[r2][c2] - prefix[r2][c1-1] - prefix[r1-1][c2] + prefix[r1-1][c1-1];
			bw.write(sum + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}