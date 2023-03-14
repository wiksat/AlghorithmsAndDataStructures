from egzP9btesty import runtests


def Euler(adj):
	edge_count = dict()
	for i in range(len(adj)):
		edge_count[i] = len(adj[i])
	if len(adj) == 0:
		return
	curr_path = []
	circuit = []
	curr_path.append(0)
	curr_v = 0 

	while len(curr_path):
		if edge_count[curr_v]:
			curr_path.append(curr_v)
			next_v = adj[curr_v][-1]
			edge_count[curr_v] -= 1
			adj[curr_v].pop()
			curr_v = next_v
		else:
			circuit.append(curr_v)
			curr_v = curr_path[-1]
			curr_path.pop()

	return circuit

def sol(G, Q):
	A = [[0 for _ in range(len(G))] for _ in range(len(G))]
	for i in range(len(G)):
		for j in G[i]:
			A[i][j] += 1
		for j in Q[i]:
			A[i][j] -= 1

	T = [[] for _ in range(len(G))]
	for i in range(len(G)):
		for j in range(len(G)):
			for _ in range(A[i][j]):
				T[i].append(j)

	return Euler(T)[::-1]
	
runtests(sol, all_tests=True)
