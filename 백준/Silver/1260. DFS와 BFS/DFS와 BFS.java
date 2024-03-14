import java.io.*;
import java.util.*;

public class Main {
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken()) + 1;
		int m = Integer.parseInt(st.nextToken());
		int v = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList[n];
		for(int i=0; i<n; i++)
			graph[i] = new ArrayList<Integer>();
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			graph[a].add(b);
			graph[b].add(a);
		}
		
		for(int i=0; i<n; i++)
			Collections.sort(graph[i]);
		
		visited = new boolean[n];
		visited[v] = true;
		dfs(v);
		System.out.println();
		
		visited = new boolean[n];
		visited[v] = true;
		bfs(v);
	}
	
	public static void dfs(int x) {
		System.out.printf("%d ", x);
		for(int i=0; i<graph[x].size(); i++) {
			int next = graph[x].get(i);
			
			if(visited[next] == true)
				continue;
			
			visited[next] = true;
			dfs(next);
		}
	}
	
	public static void bfs(int x) {
		Queue<Integer> q = new LinkedList();
		q.offer(x);
		
		while(q.isEmpty() == false) {
			int a = q.poll();
			System.out.printf("%d ", a);
			
			for(int i=0; i<graph[a].size(); i++) {
				int next = graph[a].get(i);
				
				if(visited[next] == true)
					continue;
				
				visited[next] = true;
				q.offer(next);
			}
		}
	}
}