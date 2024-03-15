import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int q = Integer.parseInt(br.readLine());
		
		int size = input.length();
		int[][] prefix = new int[26][size+1];
		
		for(int i=0; i<26; i++)
			for(int j=0; j<size+1; j++)
				prefix[i][j] = 0;
		
		for(int i=0; i<size; i++) {
			int num = input.charAt(i) - 'a';
			for(int j=0; j<26; j++) {
				if(j == num)
					prefix[j][i+1] = prefix[j][i] + 1;
				else
					prefix[j][i+1] = prefix[j][i];
			}
		}
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for(int i=0; i<q; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int index = st.nextToken().charAt(0) - 'a';
			int l = Integer.parseInt(st.nextToken());
			int r = Integer.parseInt(st.nextToken());
			
			int res = prefix[index][r+1] - prefix[index][l];
			
			bw.write(res + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}