import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[][] map = new int[100][100];
		for(int i=0; i<100; i++)
			for(int j=0; j<100; j++)
				map[i][j] = 0;
		
		int n = Integer.parseInt(br.readLine());
		for(int a=0; a<n; a++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			for(int i=0; i<10; i++)
				for(int j=0; j<10; j++)
					map[x+i-1][y+j-1] = 1;
		}
		
		int[][] prefix = new int[101][101];
		for(int i=0; i<=100; i++)
			for(int j=0; j<=100; j++) {
				if(i == 0 || j == 0)
					prefix[i][j] = 0;
				else
					prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + map[i-1][j-1];
			}
		
		int maxSize = 0;
		for(int i=1; i<=100; i++)
			for(int j=1; j<=100; j++)
				for(int x=1; x<=i; x++)
					for(int y=1; y<=j; y++) {
						int sum = prefix[i][j] - prefix[i-x][j] - prefix[i][j-y] + prefix[i-x][j-y];
						
						if(sum == x * y)
							maxSize = Math.max(maxSize,  x*y);
					}
		
		System.out.println(maxSize);
	}
}