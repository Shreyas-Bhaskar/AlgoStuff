import numpy as np

inf = np.inf

def extend_shortest_paths(L, W):
    n = L.shape[0]
    new_L = np.full((n, n), inf)
    for i in range(n):
        for j in range(n):
            new_L[i, j] = min(new_L[i, j], *(L[i, k] + W[k, j] for k in range(n)))
    return new_L

def slow_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = [W]
    for m in range(1, n):
        L.append(extend_shortest_paths(L[m - 1], W))
    return L

def faster_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = [W]
    m = 1
    while m < n - 1:
        L.append(extend_shortest_paths(L[-1], L[-1]))
        m = 2 * m
    return L

def to_latex_bmatrix(matrix):
    lines = str(np.matrix(matrix)).replace('[', '').replace(']', '').splitlines()
    latex = "\\begin{bmatrix}\n"
    latex += "\\\\\n".join([" & ".join(line.split()) for line in lines])
    latex += "\n\\end{bmatrix}"
    return latex.replace('inf', '\\infty')

# Example adjacency matrix
W = np.array([
    [0,     inf, inf, 2,     inf, inf],
    [1,     0,   inf, inf,   inf, inf],
    [inf,   2,   0,   inf,   inf, -8 ],
    [-4,    inf, inf, 0,     3,   inf],
    [inf,   7,   inf, inf,   0,   inf],
    [inf,   5,   10,  inf,   inf, 0  ]
])

slow_matrices = slow_all_pairs_shortest_paths(W)
faster_matrices = faster_all_pairs_shortest_paths(W)

# Generate LaTeX code for the resulting matrices
print("\\section*{SLOW-ALL-PAIRS-SHORTEST-PATHS}")
for i, matrix in enumerate(slow_matrices, start=1):
    print(f"\\subsection*{{Matrix after iteration {i}}}")
    print(to_latex_bmatrix(matrix))
    print("\n")

print("\\section*{FASTER-ALL-PAIRS-SHORTEST-PATHS}")
for i, matrix in enumerate(faster_matrices, start=1):
    print(f"\\subsection*{{Matrix after iteration {i}}}")
    print(to_latex_bmatrix(matrix))
    print("\n")
