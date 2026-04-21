import sys
import os
import pygame
import time

# Thêm thư mục gốc (TH) vào danh sách tìm kiếm thư viện của Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from maps.maze_basic import maze as basic_maze
from maps.maze_hard import maze as hard_maze
from src.bfs_solver import bfs
from src.dfs_solver import dfs

# Pygame Setup
CELL_SIZE = 40
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (200, 200, 200)
START_COLOR = (0, 255, 0)
GOAL_COLOR = (255, 0, 0)
SOLUTION_COLOR = (0, 0, 255)
VISITED_COLOR = (255, 255, 0)

def draw_maze(screen, maze, path=None, visited=None):
    """Vẽ mê cung lên pygame screen"""
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if maze[r][c] == 1:  # Tường
                pygame.draw.rect(screen, WALL_COLOR, rect)
            elif maze[r][c] == 'S':  # Start
                pygame.draw.rect(screen, START_COLOR, rect)
                pygame.draw.circle(screen, (0, 150, 0), rect.center, 8)
            elif maze[r][c] == 'G':  # Goal
                pygame.draw.rect(screen, GOAL_COLOR, rect)
                pygame.draw.circle(screen, (200, 0, 0), rect.center, 8)
            else:  # Đường đi
                pygame.draw.rect(screen, PATH_COLOR, rect)
            
            # Vẽ visited
            if visited and (r, c) in visited and maze[r][c] not in ['S', 'G']:
                pygame.draw.rect(screen, VISITED_COLOR, rect)
            
            pygame.draw.rect(screen, (100, 100, 100), rect, 1)  # Viền
    
    # Vẽ đường giải
    if path:
        for r, c in path[1:-1]:  # Bỏ qua Start và Goal
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, SOLUTION_COLOR, rect)
            pygame.draw.circle(screen, (0, 0, 150), rect.center, 5)

def visualize_maze(maze, algorithm_name, algorithm_func):
    """Khởi động pygame và hiển thị mê cung"""
    pygame.init()
    
    width = len(maze[0]) * CELL_SIZE
    height = len(maze) * CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f"{algorithm_name}")
    clock = pygame.time.Clock()
    
    result = algorithm_func(maze)
    path, visited = result if result[0] is not None else (result[0], result[1])
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        draw_maze(screen, maze, path, visited)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    print("\n========== BẢN ĐỒ CƠ BẢN ==========")
    print(">>> CHẠY THUẬT TOÁN BFS:")
    print("(Cửa sổ Pygame sẽ hiển thị, đóng để tiếp tục)")
    visualize_maze(basic_maze, "BFS - Bản đồ cơ bản", bfs)
    
    print("\n>>> CHẠY THUẬT TOÁN DFS:")
    print("(Cửa sổ Pygame sẽ hiển thị, đóng để tiếp tục)")
    visualize_maze(basic_maze, "DFS - Bản đồ cơ bản", dfs)
    
    print("\n========== BẢN ĐỒ KHÓ (10x10) ==========")
    print(">>> CHẠY THUẬT TOÁN BFS:")
    print("(Cửa sổ Pygame sẽ hiển thị, đóng để tiếp tục)")
    visualize_maze(hard_maze, "BFS - Bản đồ khó", bfs)
    
    print("\n>>> CHẠY THUẬT TOÁN DFS:")
    print("(Cửa sổ Pygame sẽ hiển thị, đóng để tiếp tục)")
    visualize_maze(hard_maze, "DFS - Bản đồ khó", dfs)