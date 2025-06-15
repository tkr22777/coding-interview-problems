# Grid & Matrix Exploration

<details>
<summary><strong>💡 Grid Problem Patterns</strong></summary>

```python
# 🎯 GRID PROBLEM IDENTIFICATION:
# Keywords: "2D matrix", "grid", "board", "maze", "islands"
# Common patterns: "connected components", "flood fill", "shortest path"
# Structure: Usually requires DFS/BFS traversal with direction vectors

# ✅ BEST PRACTICES FOR GRID PROBLEMS:
# 1. Use helper functions to avoid nested loops
# 2. Create separate functions for bounds checking
# 3. Use direction vectors for cleaner neighbor iteration
# 4. Handle visited tracking consistently
# 5. Separate exploration logic from boundary/validation logic

# 🚨 AVOID THESE ANTI-PATTERNS:
# - 3-4 nested loops for exploration
# - Inline bounds checking in main logic
# - Copy-paste code for different directions
# - Mixed exploration and validation logic
```

</details>

<details>
<summary><strong>Grid Traversal Foundation</strong></summary>

```python
# 🏗️ REUSABLE GRID HELPER FUNCTIONS

def is_valid_cell(grid, row, col):
    """Check if cell coordinates are within grid bounds"""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def get_neighbors(row, col):
    """Get 4-directional neighbors (up, right, down, left)"""
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return [(row + dr, col + dc) for dr, dc in directions]

def get_neighbors_8dir(row, col):
    """Get 8-directional neighbors (including diagonals)"""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    return [(row + dr, col + dc) for dr, dc in directions]

def grid_dfs_template(grid, start_row, start_col, visited, condition_func):
    """
    Template for DFS-based grid exploration
    condition_func: returns True if cell should be explored
    """
    if not is_valid_cell(grid, start_row, start_col):
        return
    
    if (start_row, start_col) in visited:
        return
    
    if not condition_func(grid, start_row, start_col):
        return
    
    visited.add((start_row, start_col))
    
    # Process current cell (customize this part)
    # ... your logic here ...
    
    # Explore neighbors
    for next_row, next_col in get_neighbors(start_row, start_col):
        grid_dfs_template(grid, next_row, next_col, visited, condition_func)
```

</details>

<details>
<summary><strong>Connected Components & Islands</strong></summary>

```python
# 🏝️ ISLAND/REGION COUNTING PROBLEMS

def count_islands(grid):
    """Count number of connected islands (1s surrounded by water 0s)"""
    if not grid or not grid[0]:
        return 0
    
    def is_land(grid, row, col):
        return grid[row][col] == '1'
    
    def explore_island(grid, row, col, visited):
        """DFS to mark entire island as visited"""
        if not is_valid_cell(grid, row, col):
            return
        if (row, col) in visited or not is_land(grid, row, col):
            return
        
        visited.add((row, col))
        
        # Explore all 4 directions
        for next_row, next_col in get_neighbors(row, col):
            explore_island(grid, next_row, next_col, visited)
    
    visited = set()
    island_count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and is_land(grid, row, col):
                explore_island(grid, row, col, visited)
                island_count += 1
    
    return island_count

def max_island_area(grid):
    """Find the area of the largest island"""
    def explore_and_count(grid, row, col, visited):
        """DFS that returns the area of current island"""
        if not is_valid_cell(grid, row, col):
            return 0
        if (row, col) in visited or grid[row][col] == 0:
            return 0
        
        visited.add((row, col))
        area = 1  # Current cell
        
        # Add area from neighbors
        for next_row, next_col in get_neighbors(row, col):
            area += explore_and_count(grid, next_row, next_col, visited)
        
        return area
    
    visited = set()
    max_area = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited and grid[row][col] == 1:
                area = explore_and_count(grid, row, col, visited)
                max_area = max(max_area, area)
    
    return max_area

def surrounded_regions(board):
    """Capture regions surrounded by 'X' (flip 'O' to 'X')"""
    if not board or not board[0]:
        return
    
    def mark_safe_regions(board, row, col):
        """Mark regions connected to border as safe (temp mark)"""
        if not is_valid_cell(board, row, col) or board[row][col] != 'O':
            return
        
        board[row][col] = 'SAFE'  # Temporary marker
        
        for next_row, next_col in get_neighbors(row, col):
            mark_safe_regions(board, next_row, next_col)
    
    rows, cols = len(board), len(board[0])
    
    # Mark all border-connected 'O's as safe
    for row in range(rows):
        for col in [0, cols - 1]:  # Left and right borders
            if board[row][col] == 'O':
                mark_safe_regions(board, row, col)
    
    for col in range(cols):
        for row in [0, rows - 1]:  # Top and bottom borders
            if board[row][col] == 'O':
                mark_safe_regions(board, row, col)
    
    # Convert unmarked 'O's to 'X', restore safe ones to 'O'
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            elif board[row][col] == 'SAFE':
                board[row][col] = 'O'
```

</details>

<details>
<summary><strong>Shortest Path in Grids</strong></summary>

```python
# 🎯 BFS FOR SHORTEST PATH IN GRIDS

from collections import deque

def shortest_path_binary_maze(maze, start, end):
    """Find shortest path in binary maze (0=walkable, 1=wall)"""
    if not maze or not maze[0]:
        return -1
    
    start_row, start_col = start
    end_row, end_col = end
    
    if maze[start_row][start_col] == 1 or maze[end_row][end_col] == 1:
        return -1
    
    def is_walkable(maze, row, col):
        return is_valid_cell(maze, row, col) and maze[row][col] == 0
    
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited = {(start_row, start_col)}
    
    while queue:
        row, col, dist = queue.popleft()
        
        if row == end_row and col == end_col:
            return dist
        
        for next_row, next_col in get_neighbors(row, col):
            if (next_row, next_col) not in visited and is_walkable(maze, next_row, next_col):
                visited.add((next_row, next_col))
                queue.append((next_row, next_col, dist + 1))
    
    return -1

def shortest_path_with_obstacles(grid, k):
    """Shortest path with ability to eliminate up to k obstacles"""
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    if rows == 1 and cols == 1:
        return 0
    
    # State: (row, col, obstacles_used, distance)
    queue = deque([(0, 0, 0, 0)])
    # Visited: (row, col, obstacles_used)
    visited = {(0, 0, 0)}
    
    while queue:
        row, col, obstacles_used, dist = queue.popleft()
        
        for next_row, next_col in get_neighbors(row, col):
            if not is_valid_cell(grid, next_row, next_col):
                continue
            
            # Calculate new obstacle count
            new_obstacles = obstacles_used + grid[next_row][next_col]
            if new_obstacles > k:
                continue
            
            if next_row == rows - 1 and next_col == cols - 1:
                return dist + 1
            
            state = (next_row, next_col, new_obstacles)
            if state not in visited:
                visited.add(state)
                queue.append((next_row, next_col, new_obstacles, dist + 1))
    
    return -1

def walls_and_gates(rooms):
    """Fill rooms with distance to nearest gate (multi-source BFS)"""
    if not rooms or not rooms[0]:
        return
    
    INF = 2147483647
    queue = deque()
    
    # Find all gates (value 0) as starting points
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                queue.append((row, col, 0))
    
    def is_empty_room(rooms, row, col):
        return (is_valid_cell(rooms, row, col) and 
                rooms[row][col] == INF)
    
    while queue:
        row, col, dist = queue.popleft()
        
        for next_row, next_col in get_neighbors(row, col):
            if is_empty_room(rooms, next_row, next_col):
                rooms[next_row][next_col] = dist + 1
                queue.append((next_row, next_col, dist + 1))
```

</details>

<details>
<summary><strong>Flood Fill & Color Modification</strong></summary>

```python
# 🎨 FLOOD FILL PATTERN PROBLEMS

def flood_fill(image, sr, sc, new_color):
    """Paint bucket tool - fill connected region with new color"""
    if not image or not image[0]:
        return image
    
    original_color = image[sr][sc]
    if original_color == new_color:
        return image
    
    def fill_connected_pixels(image, row, col, original, new):
        if not is_valid_cell(image, row, col):
            return
        if image[row][col] != original:
            return
        
        image[row][col] = new
        
        for next_row, next_col in get_neighbors(row, col):
            fill_connected_pixels(image, next_row, next_col, original, new)
    
    fill_connected_pixels(image, sr, sc, original_color, new_color)
    return image

def color_border(grid, r0, c0, color):
    """Color the border of connected component"""
    if not grid or not grid[0]:
        return grid
    
    original_color = grid[r0][c0]
    if original_color == color:
        return grid
    
    def find_component_and_borders(grid, row, col, visited, component):
        if not is_valid_cell(grid, row, col):
            return
        if (row, col) in visited or grid[row][col] != original_color:
            return
        
        visited.add((row, col))
        
        # Check if this cell is on the border
        is_border = False
        neighbor_count = 0
        
        for next_row, next_col in get_neighbors(row, col):
            if is_valid_cell(grid, next_row, next_col):
                neighbor_count += 1
                if grid[next_row][next_col] != original_color:
                    is_border = True
            else:
                is_border = True  # Edge of grid is also border
        
        if is_border or neighbor_count < 4:
            component['borders'].add((row, col))
        
        # Continue exploring
        for next_row, next_col in get_neighbors(row, col):
            find_component_and_borders(grid, next_row, next_col, visited, component)
    
    visited = set()
    component = {'borders': set()}
    find_component_and_borders(grid, r0, c0, visited, component)
    
    # Color the border cells
    for row, col in component['borders']:
        grid[row][col] = color
    
    return grid

def pacific_atlantic_water_flow(heights):
    """Find cells where water can flow to both oceans"""
    if not heights or not heights[0]:
        return []
    
    rows, cols = len(heights), len(heights[0])
    
    def dfs_reachable(heights, row, col, visited, prev_height):
        if not is_valid_cell(heights, row, col):
            return
        if (row, col) in visited:
            return
        if heights[row][col] < prev_height:
            return
        
        visited.add((row, col))
        
        for next_row, next_col in get_neighbors(row, col):
            dfs_reachable(heights, next_row, next_col, visited, heights[row][col])
    
    # Find cells reachable from Pacific (top, left borders)
    pacific_reachable = set()
    for col in range(cols):
        dfs_reachable(heights, 0, col, pacific_reachable, heights[0][col])
    for row in range(rows):
        dfs_reachable(heights, row, 0, pacific_reachable, heights[row][0])
    
    # Find cells reachable from Atlantic (bottom, right borders)
    atlantic_reachable = set()
    for col in range(cols):
        dfs_reachable(heights, rows-1, col, atlantic_reachable, heights[rows-1][col])
    for row in range(rows):
        dfs_reachable(heights, row, cols-1, atlantic_reachable, heights[row][cols-1])
    
    # Return cells reachable from both oceans
    return list(pacific_reachable & atlantic_reachable)
```

</details>

<details>
<summary><strong>Advanced Grid Patterns</strong></summary>

```python
# 🧩 COMPLEX GRID EXPLORATION PATTERNS

def word_search(board, word):
    """Find if word exists in board (can move in 4 directions)"""
    if not board or not board[0] or not word:
        return False
    
    def backtrack_search(board, row, col, word, index, path):
        if index == len(word):
            return True
        
        if not is_valid_cell(board, row, col):
            return False
        if (row, col) in path:
            return False
        if board[row][col] != word[index]:
            return False
        
        # Add to path and explore
        path.add((row, col))
        
        for next_row, next_col in get_neighbors(row, col):
            if backtrack_search(board, next_row, next_col, word, index + 1, path):
                return True
        
        # Backtrack
        path.remove((row, col))
        return False
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                if backtrack_search(board, row, col, word, 0, set()):
                    return True
    
    return False

def shortest_path_all_keys(grid):
    """Collect all keys and reach end (state-space BFS)"""
    if not grid or not grid[0]:
        return -1
    
    from collections import deque
    
    # Find start position and count total keys
    start = None
    total_keys = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                start = (row, col)
            elif grid[row][col].islower():
                total_keys += 1
    
    if not start:
        return -1
    
    def can_pass(cell, keys_state):
        if cell == '#':
            return False
        if cell.isupper():
            return keys_state & (1 << (ord(cell.lower()) - ord('a')))
        return True
    
    # State: (row, col, keys_bitmask, steps)
    queue = deque([(start[0], start[1], 0, 0)])
    visited = {(start[0], start[1], 0)}
    
    while queue:
        row, col, keys, steps = queue.popleft()
        
        # Check if collected all keys
        if keys == (1 << total_keys) - 1:
            return steps
        
        for next_row, next_col in get_neighbors(row, col):
            if not is_valid_cell(grid, next_row, next_col):
                continue
            
            cell = grid[next_row][next_col]
            new_keys = keys
            
            # If it's a key, collect it
            if cell.islower():
                new_keys |= (1 << (ord(cell) - ord('a')))
            
            # Check if we can pass through
            if not can_pass(cell, keys):
                continue
            
            state = (next_row, next_col, new_keys)
            if state not in visited:
                visited.add(state)
                queue.append((next_row, next_col, new_keys, steps + 1))
    
    return -1

def robot_room_cleaner(robot):
    """Clean room with robot (explore unknown grid)"""
    def clean_room(robot, x, y, direction, visited):
        """DFS exploration with backtracking"""
        robot.clean()
        visited.add((x, y))
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for i in range(4):
            # Calculate new position
            dx, dy = directions[direction]
            next_x, next_y = x + dx, y + dy
            
            if (next_x, next_y) not in visited and robot.move():
                clean_room(robot, next_x, next_y, direction, visited)
                # Backtrack: return to original position and direction
                go_back(robot)
            
            # Turn right for next direction
            robot.turnRight()
            direction = (direction + 1) % 4
    
    def go_back(robot):
        """Return to previous position"""
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
    
    clean_room(robot, 0, 0, 0, set())
```

</details> 