import java.io.*;
import java.util.*;

public class Main {	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int maxIndexX = 0;
		Map<Integer, Integer> X = new HashMap<>();
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int index = Integer.parseInt(st.nextToken());
			int val = Integer.parseInt(st.nextToken());
			
			maxIndexX = Math.max(maxIndexX, index);
			
			X.put(index, val);
		}
		
		n = Integer.parseInt(br.readLine());
		int maxIndexY = 0;
		Map<Integer, Integer> Y = new HashMap<>();
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int index = Integer.parseInt(st.nextToken());
			int val = Integer.parseInt(st.nextToken());
			
			maxIndexY = Math.max(maxIndexY, index);
			
			Y.put(index, val);
		}
		
		int a = Integer.parseInt(br.readLine());
		int b = Integer.parseInt(br.readLine());
		
		int size = Math.min(1000000001, Math.max(maxIndexX, maxIndexY+n));
		long [] prefix = new long[size];
		prefix[0] = 0;
		
		for(int i=1; i<size; i++)
			prefix[i] = prefix[i-1] + Y.getOrDefault(i-1, 0);
		
		long res = 0;
		for(int x : X.keySet()) {
			int end = x+1+b, start = x+a;
			if(end >= size)
				end = size-1;
			else if(end < 0)
				end = 0;
			
			if(start >= size)
				start = size-1;
			else if(start < 0)
				start = 0;
			
			
			long num = X.get(x) * (prefix[end] - prefix[start]);
			res += num;
		}
		
		System.out.println(res);
	}
}