from collections import deque
from src.core_logic import get_start_goal, get_neighbors, print_maze_with_path

def bfs(maze):
    start, goal = get_start_goal(maze)
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            print_maze_with_path(maze, path, len(visited))
            return path, visited
        
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None, visited