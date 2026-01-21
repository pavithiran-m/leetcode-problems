#DFS with BT

def min_knight_moves_backtracking(n, start, target):
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    visited = set()
    ans = float('inf')

    def backtrack(x, y, steps):
        nonlocal ans

        if steps >= ans:
            return

        if (x, y) == target:
            ans = steps
            return

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
                visited.add((nx, ny))
                backtrack(nx, ny, steps + 1)
                visited.remove((nx, ny))  # undo

    visited.add(start)
    backtrack(start[0], start[1], 0)

    return ans if ans != float('inf') else -1