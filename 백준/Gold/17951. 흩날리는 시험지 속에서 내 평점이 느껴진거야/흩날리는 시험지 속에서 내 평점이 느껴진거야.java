import java.io.*;
import java.util.*;

public class Main {	
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[] score = new int[n];
		st = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<n; i++)
			score[i] = Integer.parseInt(st.nextToken());
		
		int start = 0, end = 10000000;
		int maxScore = 0;
		
		while(start <= end) {
			int mid = (start + end) / 2;
			
			int cnt = 0;
			int now_score = 0;
			for(int s : score) {
				now_score += s;
				if(now_score >= mid) {
					now_score = 0;
					cnt++;
				}
			}
			
			if(cnt >= k) {
				maxScore = Math.max(maxScore, mid);
				start = mid + 1;
			} else
				end = mid - 1;
		}
		
		System.out.println(maxScore);
	}
}