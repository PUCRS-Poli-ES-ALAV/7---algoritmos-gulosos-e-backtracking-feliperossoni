import time

def isSafe(mat, row, col):
    n = len(mat)
    
    # Verifica a mesma coluna em linhas anteriores
    for i in range(row):
        if mat[i][col]:
            return False
    
    # Verifica diagonal superior esquerda
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return False
        i -= 1
        j -= 1
    
    # Verifica diagonal superior direita
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return False
        i -= 1
        j += 1
    
    return True

def placeQueens(row, mat, solutions, iterations):
    iterations[0] += 1  # Incrementa a contagem de iterações
    n = len(mat)
    
    if row == n:
        # Adiciona a solução encontrada
        solution = []
        for r in range(n):
            for c in range(n):
                if mat[r][c] == 1:
                    solution.append(c + 1)
        solutions.append(solution)
        return
    
    for col in range(n):
        if isSafe(mat, row, col):
            mat[row][col] = 1
            placeQueens(row + 1, mat, solutions, iterations)
            mat[row][col] = 0  # Backtrack

def nQueen(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    iterations = [0]  # Contador de iterações (passado por referência)
    
    start_time = time.perf_counter()
    placeQueens(0, mat, solutions, iterations)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    return solutions, iterations[0], elapsed_time

if __name__ == "__main__":
    test_cases = [7, 10, 13]
    
    for n in test_cases:
        print(f"\nTestando para n = {n}")
        solutions, iterations, time_spent = nQueen(n)
        
        print(f"Tempo gasto: {time_spent:.4f} segundos")
        print(f"Número de iterações: {iterations}")
        print(f"Soluções encontradas: {len(solutions)}")
        
        # Opcional: mostrar a primeira solução (se existir)
        if len(solutions) > 0:
            print("Primeira solução:", " ".join(map(str, solutions[0])))