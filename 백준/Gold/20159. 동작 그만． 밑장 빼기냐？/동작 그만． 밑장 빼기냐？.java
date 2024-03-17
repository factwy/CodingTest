import java.io.*;
import java.util.*;

public class Main {
	final static int maxTime = 2100000000;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int[] prefixOdd = new int[n+1];
		int[] prefixEven = new int[n+1];
		prefixOdd[0] = 0;
		prefixEven[0] = 0;
		
		int lastCard = 0;
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for(int i=1; i<=n; i++) {
			int card = Integer.parseInt(st.nextToken());
			
			prefixOdd[i] = prefixOdd[i-1];
			prefixEven[i] = prefixEven[i-1];
			
			if(i % 2 == 0)
				prefixEven[i] += card;
			else
				prefixOdd[i] += card;
			
			lastCard = card;
		}
		
		int maxCard = prefixOdd[n];
		for(int i=1; i<=n; i++) {
			int myLast = prefixOdd[i-1] + lastCard + prefixEven[n-1] - prefixEven[i];
			int notMyLast = prefixOdd[i-1] + prefixEven[n-2] - prefixEven[i-1];
			maxCard = Math.max(maxCard, Math.max(myLast, notMyLast));
		}
		
		System.out.println(maxCard);
	}
}